import asyncio
import os

from mistralai import Mistral
from mistralai.models import UserMessage, AssistantMessage


async def main():
    """
    Main function.
    """

    client = create_client()
    history = []

    print("Welcome to the Mistral AI interpreter!")
    print("Type 'exit' to quit.\n")

    while True:
        message = get_user_input()

        if message == "exit":
            break

        history.append(UserMessage(content=message))

        await chat(client, history)
        print("\n")


def create_client() -> Mistral:
    """
    Create a Mistral client with the API key from the environment.
    """

    api_key = os.environ["MISTRAL_API_KEY"]
    return Mistral(api_key=api_key)


def get_user_input():
    """
    Get user input from the command line.
    """

    user_input = input("You: ")

    if user_input.strip() == "":
        return get_user_input()

    return user_input


async def chat(client: Mistral, history: list, model: str = "mistral-tiny"):
    """
    Chat with Mistral AI.¬

    Args:
        client (Mistral): The Mistral client.
        message (str): The message to send to the model.
        model (str): The model to use for the chat.
    """

    response = await client.chat.stream_async(
        model=model,
        messages=history,
    )

    assistant_response = ""

    print("\nMistral:", end=" ")
    async for chunk in response:
        if chunk.data.choices[0].delta.content is not None:
            content = chunk.data.choices[0].delta.content
            print(content, end="")
            assistant_response += content

    history.append(AssistantMessage(content=assistant_response))


if __name__ == "__main__":
    asyncio.run(main())


def run_main():
    import asyncio
    from mistral_interpreter.chatbot import main

    asyncio.run(main())
