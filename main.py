import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from generate_content import generate_content

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
MAX_ITERATIONS = 20


def main():
    flag_verbose = False
    nb_args = len(sys.argv)

    # 1. Parse the arguments
    if nb_args <= 1:
        print("AI Agent App:")
        print(f'Usage: python3 {sys.argv[0]} "prompt" [--verbose]')
        print("Example: python main.py what is the meaning of life ?")
        exit(1)

    if sys.argv[nb_args - 1] in ["--verbose", "-v"]:
        flag_verbose = True
        sys.argv[nb_args - 1] = ""

    # 2. Create client, construct the initial prompt and config
    client = genai.Client(api_key=API_KEY)
    user_prompt = " ".join(sys.argv[1:])
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    # 3. Generate result and print it
    for i in range(0, MAX_ITERATIONS):
        if generate_content(client, messages, flag_verbose) == "Done":
            break


if __name__ == "__main__":
    main()
