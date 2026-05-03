# Chat roles and system messages
# Building conversations with the OpenAI API unlocks powerful ways to create interactive AI applications. This lesson will help you understand how to guide chat models effectively using roles and system messages.

from dotenv import load_dotenv
import os
from openai import OpenAI

# Load variables from .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  max_completion_tokens=150,
  messages=[
    {"role": "system",
     "content": "You are a study planning assistant that creates plans for learning new skills."},
    {"role": "user",
     "content": "I want to learn to speak Dutch."}
  ]
)

# Extract the assistant's text response
print(response.choices[0].message.content)


#System Role Example
sys_msg = """You are a study planning assistant that creates plans for learning new skills.

If these skills are non related to languages, return the message:

'Apologies, to focus on languages, we no longer create learning plans on other topics.'
"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": sys_msg},
    {"role": "user", "content": "Help me learn to jet sking."}
  ]
)

print(response.choices[0].message.content)


