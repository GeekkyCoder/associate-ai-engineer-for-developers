client = OpenAI(api_key="<OPENAI_API_TOKEN>")

function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""
Modify the Python function delimited by triple backticks by following these steps:

1. Check whether the width and length inputs are positive numbers.
2. If either input is not positive, display an appropriate error message.
3. Otherwise, calculate the area and perimeter of the rectangle.
4. Return both the area and perimeter from the function.
5. Keep the code clear and readable.

```python
{function}
```
"""

response = get_response(prompt)
print(response)




# Output 
# Here's the modified Python function that incorporates the requested changes:

# ```python
# def calculate_area_rectangular_floor(width, length):
#     # Check if width and length are positive numbers
#     if width <= 0 or length <= 0:
#         return "Error: Width and length must be positive numbers."
    
#     # Calculate area and perimeter
#     area = width * length
#     perimeter = 2 * (width + length)
    
#     return area, perimeter
# ```

# ### Explanation of Changes:
# 1. **Input Validation**: The function checks if `width` and `length` are positive numbers. If not, it returns an error message.
# 2. **Area and Perimeter Calculation**: If the inputs are valid, it calculates both the area and perimeter of the rectangle.
# 3. **Return Values**: The function returns both the area and perimeter as a tuple.
# 4. **Code Clarity**: The code is structured clearly with comments to enhance readability.

# <script.py> output:
#     Here's the modified Python function that incorporates the requested changes:
    
#     ```python
#     def calculate_area_rectangular_floor(width, length):
#         # Check if width and length are positive numbers
#         if width <= 0 or length <= 0:
#             return "Error: Width and length must be positive numbers."
        
#         # Calculate area and perimeter
#         area = width * length
#         perimeter = 2 * (width + length)
        
#         return area, perimeter
#     ```
    
#     ### Explanation of Changes:
#     1. **Input Validation**: The function checks if `width` and `length` are positive numbers. If not, it returns an error message.
#     2. **Area and Perimeter Calculation**: If the inputs are valid, it calculates both the area and perimeter of the rectangle.
#     3. **Return Values**: The function returns both the area and perimeter as a tuple.
#     4. **Code Clarity**: The code is structured clearly with comments to enhance readability.