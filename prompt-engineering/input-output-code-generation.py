client = OpenAI(api_key="<OPENAI_API_TOKEN>")

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt =f""" 
write a python function that maps the inputs to the outputs, delimitted by triple backticks:
```{examples}```
"""

response = get_response(prompt)
print(response)



# Output 
# Here is the Python function that implements this logic:

# ```python
# def map_inputs_to_output(inputs):
#     return sum(inputs)

# # Example usage:
# print(map_inputs_to_output([10, 5, 8]))  # Output: 23
# print(map_inputs_to_output([5, 2, 4]))    # Output: 11
# print(map_inputs_to_output([2, 1, 3]))    # Output: 6
# print(map_inputs_to_output([8, 4, 6]))    # Output: 18
# ```

# This function takes a list of integers as input and returns the sum of those integers, which matches the outputs provided in your examples.