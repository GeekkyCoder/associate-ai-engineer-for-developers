client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = """you are a customer service chatbot that supports customers for a delivery service with whatever they need from the following: 
 - such as groceries, medications, and documents to larger items like electronics, clothing, and furniture.

when answering to customer, always use a gentle tone.
"""

context_question = "What types of items can be delivered using MyPersonalDelivery?"
context_answer = "We deliver everything from everyday essentials such as groceries, medications, and documents to larger items like electronics, clothing, and furniture. However, please note that we currently do not offer delivery for hazardous materials or extremely fragile items requiring special handling."

# Add the context to the model
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "system", "content": system_prompt},
            {"role": "user", "content": context_question},
            {"role": "assistant", "content": context_answer },
            {"role": "user", "content": "Do you deliver furniture?"}])
response = response.choices[0].message.content
print(response)



# <script.py> output:
#     Yes, we do offer furniture delivery! Whether you need a cozy chair, a stylish table, or a complete set of furniture, we're here to assist you. If you have a specific item in mind, feel free to let me know, and I can guide you through the process!
