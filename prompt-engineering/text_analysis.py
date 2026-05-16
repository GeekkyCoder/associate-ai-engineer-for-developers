client = OpenAI(api_key="<OPENAI_API_TOKEN>")

ticket= """ 
Subject: Urgent - Login Error

Hi Support Team,

I'm having trouble accessing my account with the username "example_user." Every time I try to log in, I encounter an error message. I've already attempted to reset my password, but the issue persists. I need to resolve this problem urgently, as I have pending tasks that require immediate attention.

Please investigate and assist promptly.

Thanks,
John.

Class:  Technical Issue

"""

# Craft a prompt to classify the ticket
prompt = f"""
You are a customer support ticket classifier.

Classify the ticket into exactly ONE of the following categories:

1. Technical Issue  
2. Billing Inquiry  
3. Product Feedback  

### Rules:
- Output ONLY the category name.
- Do NOT include explanations or extra text.
- Choose the best match even if multiple categories seem relevant.

### Ticket:
```{ticket}```
"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)



# <script.py> output:
#     Ticket:  
#     Subject: Urgent - Login Error
    
#     Hi Support Team,
    
#     I'm having trouble accessing my account with the username "example_user." Every time I try to log in, I encounter an error message. I've already attempted to reset my password, but the issue persists. I need to resolve this problem urgently, as I have pending tasks that require immediate attention.
    
#     Please investigate and assist promptly.
    
#     Thanks,
#     John.
    
#     Class:  Technical Issue
# In [1]:


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a few-shot prompt to get the ticket's entities
prompt = f"""
Extract the key entities from the customer support ticket.
Return the output as a JSON object with the following keys:
- customer_name
- issue_type
- product
- urgency
- channel

Examples:

Ticket: {ticket_1}
Entities: {entities_1}

Ticket: {ticket_2}
Entities: {entities_2}

Ticket: {ticket_3}
Entities: {entities_3}

Now analyze the following ticket and extract the entities.

Ticket: {ticket_4}

Entities:
"""

response = get_response(prompt)
print("Ticket: ", ticket_4)
print("Entities: ", response)


#Output:
# Ticket: 
#  Greetings, I am facing technical difficulties with your software, ABC Editor. My name is Sarah Lee, and I recently upgraded to the latest version. However, whenever I try to save my work, the software crashes. Can you please help me resolve this problem?
# Entities: 
#  ```json
# {
#   "customer_name": "Sarah Lee",
#   "issue_type": "technical difficulties",
#   "product": "ABC Editor",
#   "urgency": "high",
#   "channel": "email"
# }
# ```

# <script.py> output:
#     Ticket: 
#      Greetings, I am facing technical difficulties with your software, ABC Editor. My name is Sarah Lee, and I recently upgraded to the latest version. However, whenever I try to save my work, the software crashes. Can you please help me resolve this problem?
#     Entities: 
#      ```json
#     {
#       "customer_name": "Sarah Lee",
#       "issue_type": "technical difficulties",
#       "product": "ABC Editor",
#       "urgency": "high",
#       "channel": "support ticket"
#     }
#     ```