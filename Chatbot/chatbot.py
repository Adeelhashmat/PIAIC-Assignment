import chainlit as cl
import json
from datetime import datetime
from my_secrets import Secrets
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_api, set_tracing_disabled, OpenAIChatCompletionsModel

# Global variable to store chat history
chat_history = []

@cl.on_message
async def main(msg: cl.Message):
    secrets = Secrets()

    external_client = AsyncOpenAI(
        api_key=secrets.get_api_key(),
        base_url=secrets.get_api_base_url(),
    )
    set_tracing_disabled(True)
    set_default_openai_api(external_client)

    agent = Agent(
        name="Assistant",
        instructions="Answer the question as best as you can.",
        model=OpenAIChatCompletionsModel(
            model=secrets.get_api_model(),
            openai_client=external_client,
        ),
    )

    result = Runner.run_sync(
        starting_agent=agent,
        input=msg.content,
    )

    response = result.final_output

    # Save user input and response to history
    chat_history.append({
        "user": msg.content,
        "assistant": response
    })

    # Send message to user
    message = cl.Message(content=response)
    await message.send()

@cl.on_stop
async def on_stop():
    # Save chat history to a JSON file when session ends
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"chat_history_{timestamp}.json"
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(chat_history, f, indent=4)

    print(f"Chat history saved to {filename}")
