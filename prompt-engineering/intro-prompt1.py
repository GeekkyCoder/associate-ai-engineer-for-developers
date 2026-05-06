client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that follows the instructions
prompt = "write a poem about chatgpt using english that a child can understand"

# Get the response
response = get_response(prompt)

print(response)