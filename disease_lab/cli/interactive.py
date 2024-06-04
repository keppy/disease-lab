import os
from typing import Optional
from typing_extensions import Annotated
import asyncio
import typer
import openai
from getpass import getpass
from rich import print

if os.getenv("OPENAI_API_KEY") is None:
    print("No OPEN_API_KEY found in environment variables.")
    print("Consider setting it in your environment variables via .zshrc or .bashrc")
    print("Or you can paste it here and it will be used only for this session.")
    print("If you want to use Ollama, set OPEN_API_KEY to 'ollama'.")
    os.environ["OPENAI_API_KEY"] = getpass("Paste your OpenAI key from: https://platform.openai.com/account/api-keys\n")
    openai.api_key = os.getenv("OPENAI_API_KEY", "")

from disease_lab.entity_extraction.disease_query import expand_disease_query

app = typer.Typer()

@app.command(
    "interactive",
    help="Starts an interactive session with the AI.",
)
def interactive(model: Annotated[Optional[str], typer.Argument()] = None):
    if os.getenv("OPENAI_API_KEY") == "ollama" or model == "ollama" or model == "llama3":
        print("You are using Ollama for this session.")
        print("You can ask questions about diseases and get answers from the AI.")
        print("Type 'exit' to quit the program.")
        while True:
            question = typer.prompt("Ask a question about a disease:")
            if question == "exit":
                break
            diseases = asyncio.run(expand_disease_query(question, model="llama3"))
            print(diseases)
        return

    print("Welcome to the Disease Lab interactive mode!")
    print("You can ask questions about diseases and get answers from the AI.")
    print("Type 'exit' to quit the program.")
    while True:
        question = typer.prompt("Ask a question about a disease:")
        if question == "exit":
            break
        diseases = asyncio.run(expand_disease_query(question))
        print(diseases)
