# Single-step prompt to plan a trip
# Imagine you're a developer taking a break and you want to apply your prompting skills to plan the perfect beach vacation. As an initial step, you decide to use a standard single-step prompt to seek assistance.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a single-step prompt to get help planning the vacation
prompt = """
create a beach vacation plan for me
"""

response = get_response(prompt)
print(response)