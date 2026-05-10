# Analyze solution correctness
# You're back from your relaxing vacation and you've been assigned the task of reviewing and correcting some programming tasks, including a function to calculate of the area of a shape. You are provided with a code string that contains the function to calculate the area of a rectangle, and need to assess its correctness. The ideal function for you is a function that has correct syntax, receives two inputs, and returns one output.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f""" 
  given a function calculate_rectangle_area delimitted by triple backticks , takes 2 inputs as numbers and generate single output, analize the syntax correction, output evaluation, handling of edge cases:
  ```{code}```
"""

response = get_response(prompt)
print(response)