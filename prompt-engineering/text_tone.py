client = OpenAI(api_key="<OPENAI_API_TOKEN>")

sample_email = """ 
Subject: Check out our latest products!

Dear Customer,

We are excited to introduce our latest product line that includes a wide range of items to suit your needs. Whether you're looking for electronics, home appliances, or fashion accessories, we have it all!

Hurry and visit our website to explore the fantastic deals and discounts we have for you. Don't miss out on the opportunity to get the best products at unbeatable prices.

Thank you for being a valued customer, and we look forward to serving you soon!

Best regards,
The Marketing Team
"""
prompt = f"""
Given the sample email delimited by triple backticks, rewrite the email in a professional, positive, and user-centric tone while preserving the original intent and key information.

```{sample_email}```
"""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)



# output
#  After transformation: 
#      Subject: Discover Our Exciting New Product Line!
    
#     Dear Valued Customer,
    
#     We are thrilled to share our latest product line with you, featuring a diverse selection of items designed to meet your needs. From cutting-edge electronics to stylish home appliances and fashionable accessories, we have something for everyone!
    
#     We invite you to visit our website and explore the fantastic deals and discounts currently available. This is a wonderful opportunity to find high-quality products at exceptional prices.
    
#     Thank you for being a valued member of our community. We look forward to serving you and helping you find the perfect items!
    
#     Warm regards,  
#     The Marketing Team







client = OpenAI(api_key="<OPENAI_API_TOKEN>")


text ="We are happy to inform you that your request has been processed successfully. please check your email for further details and let us know if you face any issue. thank you for choosing our service we appreciate your support."

# Craft a prompt to transform the text
prompt = f""" 
You are an expert editor and communication specialist.

Your task is to process the provided text in two sequential steps:

Step 1 — Proofreading
- Correct grammar, spelling, punctuation, and sentence clarity.
- Do NOT change the original structure, formatting, paragraph order, or intent.
- Preserve all technical terms, placeholders, names, and formatting exactly as provided.
- Only make corrections that improve readability and correctness.

Step 2 — Tone Adjustment
- Rewrite the proofread version to make the tone:
  - Formal
  - Professional
  - Friendly
  - Clear and user-centric
- Maintain the original meaning and structure as closely as possible.
- Avoid sounding overly robotic or overly casual.

Return the output in the following format:

Proofread Version:
```{text}```
"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)


#Output
# <script.py> output:
#     Before transformation:
#      We are happy to inform you that your request has been processed successfully. please check your email for further details and let us know if you face any issue. thank you for choosing our service we appreciate your support.
#     After transformation:
#      Proofread Version:
#     ```We are happy to inform you that your request has been processed successfully. Please check your email for further details and let us know if you face any issues. Thank you for choosing our service; we appreciate your support.```
    
#     Tone Adjusted Version:
#     ```We are pleased to inform you that your request has been successfully processed. Kindly check your email for further details, and do not hesitate to reach out if you encounter any issues. Thank you for choosing our service; we truly appreciate your support.```