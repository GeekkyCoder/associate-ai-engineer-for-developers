client = OpenAI(api_key="<OPENAI_API_TOKEN>")


function 

# Craft a chain-of-thought prompt that asks the model to explain what the function does
prompt = f""" 
explain the code delimitted by triple bacticks, lets think step by step: 

1. what does the function do and what is the programming language used?
2. what does the takes as input and what it returns?
3. explain the edge cases

function:
```{function}```
"""
 
response = get_response(prompt)
print(response)


# Output 
# Let's break down the provided code step by step:

# ### 1. What does the function do and what is the programming language used?

# The function `analyze_portfolio` is written in Python. It analyzes a portfolio of financial assets by calculating the total value, highest value, lowest value, and average value of the assets in the portfolio. 

# ### 2. What does it take as input and what does it return?

# **Input:**
# - The function takes a single argument, `portfolio_data`, which is expected to be a list of tuples (or lists). Each tuple (or list) represents an asset in the portfolio, where the second element (index 1) of each tuple (or list) is the value of that asset.

# **Return:**
# - The function returns a tuple containing three values:
#   1. `highest_value`: The highest value among the assets in the portfolio.
#   2. `lowest_value`: The lowest value among the assets in the portfolio.
#   3. `average_value`: The average value of the assets in the portfolio, calculated as the total value divided by the number of assets.

# ### 3. Explain the edge cases

# Here are some potential edge cases to consider:

# - **Empty Portfolio:** If `portfolio_data` is an empty list, the function will raise a `ZeroDivisionError` when it tries to calculate `average_value` because it attempts to divide by zero (the length of `portfolio_data` is zero). This should be handled to avoid runtime errors.

# - **Single Asset:** If `portfolio_data` contains only one asset, the function will correctly return that asset's value as both the highest and lowest value, and the average will be equal to that asset's value.

# - **Negative Values:** If the asset values can be negative, the function will still work correctly, but the highest and lowest values will reflect the negative values accordingly. The average will also be calculated correctly, but it may be negative if the total value is negative.

# - **Non-numeric Values:** If any of the asset values are not numeric (e.g., strings or None), the function will raise a `TypeError` when trying to perform arithmetic operations. Input validation should be added to handle such cases.

# - **Mixed Data Types:** If the portfolio contains mixed data types (e.g., some entries are tuples and others are lists), the function may not behave as expected. It assumes that each entry is a sequence with at least two elements, and the second element is numeric.

# To improve the robustness of the function, you could add checks for these edge cases, such as validating the input type and handling empty lists gracefully.

# <script.py> output:
#     Let's break down the provided code step by step:
    
#     ### 1. Function Purpose and Programming Language
#     - **Function Purpose**: The function `analyze_portfolio` is designed to analyze a portfolio of financial assets. It calculates the total value, highest value, lowest value, and average value of the assets in the portfolio.
#     - **Programming Language**: The code is written in Python.
    
#     ### 2. Inputs and Outputs
#     - **Input**: The function takes a single argument, `portfolio_data`, which is expected to be a list of tuples (or lists). Each tuple (or list) represents an asset and is assumed to contain at least two elements: the first element (not used in calculations) and the second element, which represents the value of the asset.
#       - Example of input: `[(asset1, value1), (asset2, value2), (asset3, value3)]`
      
#     - **Output**: The function returns a tuple containing three values:
#       - `highest_value`: The highest value among the assets.
#       - `lowest_value`: The lowest value among the assets.
#       - `average_value`: The average value of the assets, calculated as the total value divided by the number of assets.
    
#     ### 3. Edge Cases
#     - **Empty Portfolio**: If `portfolio_data` is an empty list, the function will raise a `ZeroDivisionError` when it tries to calculate `average_value` because it attempts to divide by zero (the length of `portfolio_data` is zero).
      
#     - **Single Asset**: If `portfolio_data` contains only one asset, the function will correctly return that asset's value as both the highest and lowest value, and the average will be equal to that value.
    
#     - **Negative Values**: If the asset values can be negative, the function will still work correctly. It will identify the highest and lowest values accordingly, but the average could also be negative.
    
#     - **Non-numeric Values**: If any of the asset values are not numeric (e.g., strings or None), the function will raise a `TypeError` when trying to perform arithmetic operations.
    
#     - **Mixed Data Types**: If the input list contains mixed data types (e.g., some entries are tuples and others are not), the function may raise an error when trying to access `entry[1]` or when performing arithmetic operations.
    
#     ### Summary
#     The `analyze_portfolio` function is a simple analysis tool for a portfolio of assets, calculating the highest, lowest, and average values. However, it is important to handle edge cases such as empty inputs and non-numeric values to ensure robustness.