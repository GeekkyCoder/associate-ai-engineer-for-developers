# Creating an AI chatbot
# To complete your POC, you'll integrate your message history with a for loop, so you can send repeated prompts to the model, storing each response in the message history in series.

# Instructions
# 100 XP
# Loop over the user messages (user_msgs).
# Create a dictionary for the user message in each iteration, and append it to messages.
# Send messages to the model in a chat request.
# Append the assistant message dictionary to messages.

from dotenv import load_dotenv
import os
from openai import OpenAI

# Load variables from .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

messages = [{"role": "system", "content": "You are a helpful math tutor that speaks concisely."}]
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

# Loop over the user questions
for q in user_msgs:
    print("User: ", q)
    
    # Create a dictionary for the user message from q and append to messages
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict)
    
    # Create the API request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=100
    )
    
    # Append the assistant's message to messages
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    messages.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n")
