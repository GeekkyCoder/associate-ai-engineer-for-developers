from dotenv import load_dotenv
import os
from openai import OpenAI

# Load variables from .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Suggest three tasks I could automate with the OpenAI API in my job."
        }
    ]
)

print(response.choices[0].message.content)