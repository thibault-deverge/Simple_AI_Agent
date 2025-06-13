from google.genai import types

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file

FUNCTION_MAP = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}

WORKING_DIRECTORY = "./calculator"


def call_function(function_call_part, verbose=False):
    name_function = function_call_part.name
    args_function = function_call_part.args

    if verbose:
        print(f"Calling function: {name_function}({args_function})")
    else:
        print(f" - Calling function: {name_function}")

    if name_function in FUNCTION_MAP:
        result = FUNCTION_MAP[name_function](WORKING_DIRECTORY, **args_function)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=name_function,
                    response={"result": result},
                )
            ],
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=name_function,
                    response={"error": f"Unknown function: {name_function}"},
                )
            ],
        )
