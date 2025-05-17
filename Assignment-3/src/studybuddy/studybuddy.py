

import os
from agents import Agent, Runner, set_default_openai_api, set_tracing_disabled, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini-compatible client
external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Set default API
set_default_openai_api(external_client)
set_tracing_disabled(True)

# Create model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-pro",
    openai_client=external_client,
)

# Create your agent
studybuddy = Agent(
    name="StudyBuddy",
    instructions="""
    You are StudyBuddy, a smart and friendly AI tutor.
    Your job is to help students understand difficult concepts,
    summarize topics, and offer effective study tips.
    Keep the tone friendly and motivational.
    Always encourage the student to ask more questions.
    """
)

# Run the agent on a test prompt
prompt = "Explain the difference between mitosis and meiosis in simple terms."
result = Runner.run_sync(studybuddy, prompt)

# Print and save the output
print(result.final_output)
with open("output.md", "w") as f:
    f.write(f"### Prompt:\n{prompt}\n\n### Response:\n{result.final_output}")
