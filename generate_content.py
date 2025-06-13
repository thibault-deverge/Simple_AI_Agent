from google.genai import types

from functions.call_function import call_function
from schemas import available_functions

SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT, tools=[available_functions]
        ),
    )

    for candidate in response.candidates:
        content = candidate.content
        messages.append(content)

    if response.function_calls:
        for call in response.function_calls:
            call_result = call_function(call, verbose)
            if call_result.parts[0].function_response.response:  # type: ignore
                messages.append(
                    types.Content(
                        role="user",
                        parts=[
                            types.Part(
                                text=call_result.parts[0].function_response.response["result"]  # type: ignore
                            )
                        ],
                    )
                )
                return "Note Done"
            else:
                raise Exception("Fatal Error calling a function")
    else:
        if verbose:
            print("User prompt:", response.text)
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)  # type: ignore
            print("Response tokens: ", response.usage_metadata.candidates_token_count)  # type: ignore
        else:
            print(response.text)
        return "Done"
