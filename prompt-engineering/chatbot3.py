client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the order number condition
order_number_condition = "provide the order number, ask for an order number if not provided."

# Define the technical issue condition
technical_issue_condition = "specify technical issue, ask the user to provide technical issue, if not provided always show empathy for users, start with I'm sorry to hear about your issue with ..."

# Create the refined system prompt
refined_system_prompt = base_system_prompt + " " + order_number_condition + " " + technical_issue_condition 

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)



# <script.py> output:
#     Response 1:  I'm sorry to hear about your issue with your laptop screen flickering. To assist you better, could you please provide more details about the technical issue? Additionally, if you have an order number for the laptop, that would be helpful as well.
#     Response 2:  Of course! I can help you with that. Could you please provide me with your order number?