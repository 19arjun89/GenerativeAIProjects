import os
import requests
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.environ.get("GROQ_API_KEY")

if groq_api_key is None:
    raise ValueError("Groq API key is not set in environment variables.")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {groq_api_key}"
}

body = {
    "model": "llama-3.1-8b-instant",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant"
        },
        {
            "role": "user",
            "content": "Tell me a very funny joke"
        }
    ]
}

response = requests.post(url, headers = headers, json = body)

if response.status_code == 200:
    print(response.json()['choices'][0]['message']['content'])
else:
    print("Error")