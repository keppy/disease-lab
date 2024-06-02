import os
import asyncio
import openai
from getpass import getpass
from prompt_toolkit import PromptSession

if os.getenv("OPENAI_API_KEY") is None:
    print("No OpenAI key found in environment variables.")
    print("Consider setting it in your environment variables via .zshrc or .bashrc")
    print("Or you can paste it here and it will be used only for this session.")
    os.environ["OPENAI_API_KEY"] = getpass("Paste your OpenAI key from: https://platform.openai.com/account/api-keys\n")
    openai.api_key = os.getenv("OPENAI_API_KEY", "")

from disease_lab.entity_extraction.disease_query import expand_disease_query

def print_disease_query_results(q) -> None:
    """Print the extracted diseases from a query"""
    response = asyncio.run(expand_disease_query(q))
    print(response.diseases)

def app():
    '''Interactive console for working with disease specific prompts.'''
    session = PromptSession()
    while True:
        try:
            text = session.prompt("> ")
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            print_disease_query_results(text)
    print("GoodBye!")
