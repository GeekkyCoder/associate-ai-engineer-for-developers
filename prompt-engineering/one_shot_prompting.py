# Controlling output structure
# One way to control the output structure provided by a language model is to give it a sample question-answer in the prompt. The model will learn from it and follow it when generating responses for similar questions. This exercise aims to let you build a one-shot prompt that extracts odd numbers from a given set of numbers and displays them as a set of numbers between brackets, separated by commas as shown in the instructions.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a one-shot prompt
prompt = """
You are given sets of numbers. Extract only the odd numbers and return them as a new set.

Example:
Input: {1, 3, 7, 12, 19}
Output: {1, 3, 7, 19}

Now solve the following:

Input: {3, 5, 11, 12, 16}
Output:
"""

response = get_response(prompt)
print(response)