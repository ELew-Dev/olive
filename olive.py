import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

def classify_message(message):
    prompt = f"What is the intent of this message: '{message}'? Choose from: Cancel, Reschedule, Complaint, Compliment, General Question."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error during classification: {e}"

def generate_response(message, intent):
    prompt = f"""You're a friendly customer support agent named Olive. A customer said: '{message}'.

The intent is: {intent}. Write a warm, helpful response."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error during response generation: {e}"
