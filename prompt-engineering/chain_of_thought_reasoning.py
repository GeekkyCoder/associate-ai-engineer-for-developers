client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the chain-of-thought prompt
prompt = """
      my friend age is 20 his father age is twice my friend's age, explain step by step what his father age will be in 10 years?
"""

response = get_response(prompt)
print(response)




# One-shot chain-of-thought prompts
# When you need to sum the even numbers within a given set, you first have to identify these even numbers and then sum them. You can teach this to a language model via one or more examples, and it will follow this strategy to operate on new sets.

# Your goal in this exercise is to teach the model how to apply this procedure on the following set: {9, 10, 13, 4, 2}, and then ask the model to perform it on a new set: {15, 13, 82, 7, 14}. This is how you perform chain-of-thought prompting through one-shot prompting.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the example 
example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
             A: Even numbers: 10,4,2. Adding them: 10+4+2=16"""

# Define the question
question = """Q:Sum the even numbers in the following set: {15, 13, 82, 7, 14}. 
              A:"""

# Create the final prompt
prompt = question + example
response = get_response(prompt)
print(response)