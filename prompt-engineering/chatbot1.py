client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": "system", "content": system_prompt  },
      		  {"role": "user", "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-4o-mini", messages= messages, temperature=0)
  
  return response.choices[0].message.content

# Try the function with a system and user prompts of your choice 
response = get_response("You are a mathematician, who answers maths related stuff, if the user asks anything other than maths, respond with iam sorry iam only a mathematician", "what is algebra")
print(response)


#Output
# Algebra is a branch of mathematics that deals with symbols and the rules for manipulating those symbols. It involves the study of mathematical expressions, equations, and the relationships between quantities. In algebra, letters (often called variables) are used to represent numbers in formulas and equations, allowing for the generalization of arithmetic operations. 

# Algebra can be divided into several subfields, including:

# 1. **Elementary Algebra**: Focuses on basic operations and the manipulation of algebraic expressions and equations.
# 2. **Abstract Algebra**: Studies algebraic structures such as groups, rings, and fields.
# 3. **Linear Algebra**: Deals with vector spaces and linear mappings between them, including the study of matrices and systems of linear equations.

# Algebra is fundamental in various areas of mathematics and is widely used in science, engineering, economics, and many other fields.

# <script.py> output:
#     Algebra is a branch of mathematics that deals with symbols and the rules for manipulating those symbols. It involves the study of mathematical expressions, equations, and the relationships between quantities. In algebra, letters (often called variables) are used to represent numbers in formulas and equations, allowing for the generalization of arithmetic operations. 
    
#     For example, in the equation \(2x + 3 = 7\), \(x\) is a variable that can represent different values. The goal in algebra is often to solve for the variable, finding its value that makes the equation true. Algebra is foundational for many areas of mathematics and is used in various applications across science, engineering, economics, and more.