from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(f"API key found: {bool(api_key)}")
print(f"API key value: {api_key}")
