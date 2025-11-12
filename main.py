import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)



def main():
    print("Hello from ai-agent-uv!")
    arguments = sys.argv[1:]
    
    if not arguments:
        print("❌ No prompt provided. Usage: python main.py 'your prompt here' [--verbose]")
        sys.exit(1)

    verbose = False
    if "--verbose" in arguments:
        verbose = True
        arguments.remove("--verbose")

    user_prompt = " ".join(arguments)

    if verbose:
        print(f'User prompt: "{user_prompt}"')

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        #apparently, the content thing automatically iterates through the list of messages
        contents= messages,
    )

    print(response.text)

    prompt_tokens = response.usage_metadata.prompt_token_count
    candidate_tokens = response.usage_metadata.candidates_token_count
    
    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {candidate_tokens}")

if __name__ == "__main__":
    main()
