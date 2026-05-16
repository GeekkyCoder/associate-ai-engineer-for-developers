client = OpenAI(api_key="<OPENAI_API_TOKEN>")

base_system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

# Define behavior guidelines
behavior_guidelines = " ask a user about their background, experience, and goals, whenever any of these is not provided in the prompt"

# Define response guidelines
response_guidelines = "recommend no more than three textbooks"

system_prompt = base_system_prompt + behavior_guidelines + response_guidelines
user_prompt = "Hey, I'm looking for courses on Python and data visualization. What do you recommend?"
response = get_response(system_prompt, user_prompt)
print(response)



# <script.py> output:
#     To provide you with the best recommendations, could you please share a bit about your background in programming and data analysis? Specifically, I'd like to know your experience level with Python and any prior knowledge you have in data visualization. Additionally, what are your specific goals for learning these topics?