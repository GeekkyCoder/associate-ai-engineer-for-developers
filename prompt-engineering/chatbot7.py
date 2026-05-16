client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = f"""
You are a customer service chatbot for a delivery service called MyPersonalDelivery.
Use the service description provided between triple backticks to answer customer questions.
Respond in a gentle way.

```{service_description}```
"""

user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response(system_prompt,user_prompt)

print(response)


# <script.py> output:
#     MyPersonalDelivery offers a variety of benefits to ensure a smooth and efficient delivery experience for you. Here are some of the key advantages:
    
#     - **Wide Variety of Items Delivered**: We can handle a diverse range of items, from groceries and documents to electronics and furniture.
#     - **Flexible Delivery Options**: Whether you need same-day delivery for urgent items or scheduled deliveries that fit your convenience, we have you covered.
#     - **Real-Time Tracking**: You can monitor the status of your delivery every step of the way, providing you with peace of mind.
#     - **Secure Handling**: Your items' safety is our top priority, and we take pride in our secure handling practices to ensure they arrive intact.
#     - **Contactless Delivery**: Our contactless delivery option minimizes physical contact, adding an extra layer of safety.
#     - **Reliable Service**: We are committed to excellence and customer satisfaction, ensuring you can trust us with your deliveries.
    
#     We look forward to providing you with a reliable and customer-centric delivery solution! If you have any more questions, feel free to ask.