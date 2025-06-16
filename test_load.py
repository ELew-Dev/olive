import os
from dotenv import load_dotenv

load_dotenv()  # this loads .env file in current directory

print("API key loaded:", os.getenv("OPENAI_API_KEY"))
