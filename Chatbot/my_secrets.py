import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_api_model = os.getenv("GEMINI_API_MODEL")
gemini_api_base_url = os.getenv("GEMINI_API_URL")

if not gemini_api_key or not gemini_api_base_url or not gemini_api_model:
    print('Please set the environment variables: GEMINI_API_KEY, GEMINI_API_MODEL, GEMINI_API_URL')
    exit(1)

class Secrets:
    def __init__(self):
        self.api_key = gemini_api_key
        self.api_model = gemini_api_model
        self.api_base_url = gemini_api_base_url

    def get_api_key(self):
        return self.api_key

    def get_api_model(self):
        return self.api_model

    def get_api_base_url(self):
        return self.api_base_url