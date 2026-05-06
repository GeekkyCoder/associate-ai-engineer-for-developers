
def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content



client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
# 1. Structured Output Generation
text = "iam a softwre engineer and aiming for cracking big tech interviews"
instructions = "Determine the language and generate a suitable title for the pre-loaded text, You are given a text delimitted by triple backticks"

# Create the output format
output_format = """Output should be in the following format:
            text: <text goes here>
            language: <language>
            title: <your generated title>
"""

# Create the final prompt
prompt = instructions + output_format + f"""{text}"""
response = get_response(prompt)
print(response)







# 2. Precise Story Generation
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to complete the story
prompt = f"""You are a Shakespearean writer.

Write a story in Shakespearean style based on the text provided between triple backticks. 
The response must contain exactly two paragraphs and no extra commentary.

```{story}```
"""







# Get the generated response
# 3. Structured Table Generation
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that generates the table
text = "Generate a table of 10 books, with columns (Title,Author,Year) and the genre should be (science fiction lover)"
instruction = "You are provided with a text delimitted by triple bacticks"
prompt =  instruction + f""" ```{text}``` """

# Get the response
response = get_response(prompt)
print(response)


