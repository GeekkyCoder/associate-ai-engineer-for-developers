client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that asks the model for the function
prompt = f""" 
write a pyhton function that recieves a list of 12 floats representing monthly sales data as input and returns the month with the highest sales value.
"""

response = get_response(prompt)
print(response)


# Output:
# ```python
# def month_with_highest_sales(sales_data):
#     if len(sales_data) != 12:
#         raise ValueError("The sales data must contain exactly 12 months of data.")
    
#     # Define the names of the months
#     months = [
#         "January", "February", "March", "April", "May", "June",
#         "July", "August", "September", "October", "November", "December"
#     ]
    
#     # Find the index of the month with the highest sales
#     max_sales_index = sales_data.index(max(sales_data))
    
#     # Return the name of the month with the highest sales
#     return months[max_sales_index]

# # Example usage:
# sales_data = [1500.0, 2000.5, 2500.0, 3000.75, 3500.0, 4000.25,
#               4500.0, 5000.5, 5500.0, 6000.75, 6500.0, 7000.25]

# highest_sales_month = month_with_highest_sales(sales_data)
# print(f"The month with the highest sales is: {highest_sales_month}")
# ```

# ### Explanation:
# 1. The function `month_with_highest_sales` takes a list of floats as input.
# 2. It checks if the length of the list is exactly 12; if not, it raises a `ValueError`.
# 3. It defines a list of month names.
# 4. It finds the index of the maximum sales value using the `max()` function and the `index()` method.
# 5. Finally, it returns the name of the month corresponding to that index.

# You can test the function with different sales data to see which month has the highest sales.
# In [1]:




client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that asks the model for the function
prompt = """
Write a Python function that takes a list of 12 numbers representing monthly sales data as input and returns the month with the highest sales.
"""

response = get_response(prompt)
print(response)


# Output
#  ```python
#     def month_with_highest_sales(sales_data):
#         if len(sales_data) != 12:
#             raise ValueError("The sales data must contain exactly 12 months of data.")
        
#         # List of month names
#         months = [
#             "January", "February", "March", "April", "May", "June",
#             "July", "August", "September", "October", "November", "December"
#         ]
        
#         # Find the index of the maximum sales
#         max_sales_index = sales_data.index(max(sales_data))
        
#         # Return the month with the highest sales
#         return months[max_sales_index]
    
#     # Example usage:
#     sales_data = [1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000]
#     highest_sales_month = month_with_highest_sales(sales_data)
#     print(f"The month with the highest sales is: {highest_sales_month}")
#     ```
    
#     ### Explanation:
#     1. The function `month_with_highest_sales` takes a list `sales_data` as input.
#     2. It checks if the length of the list is exactly 12; if not, it raises a `ValueError`.
#     3. It defines a list of month names corresponding to the indices of the sales data.
#     4. It finds the index of the maximum sales using the `max()` function and the `index()` method.
#     5. Finally, it returns the name of the month that corresponds to the highest sales.
    
#     You can test the function with different sales data to see which month has the highest sales.