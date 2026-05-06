client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = """Analyze the text provided between triple backticks. 
Determine the language of the text and count the number of sentences. 
If the text contains more than one sentence, generate a suitable title. 
If the text contains only one sentence, the title should be 'N/A'. 
"""


# Create the output format
output_format = """Provide the output in the following format, each on a new line:
Text: <original text>
Language: <language>
Number of sentences: <count>
Title: <generated title or N/A>
"""

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)