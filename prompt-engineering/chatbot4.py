client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft the system_prompt using the role-playing approach
system_prompt = "you are a learning advisor, who interpret learner queries described and provide relavent textbook recommendatons, recommend beginner and advanced textbooks based on their background, if the user asks for question which is unrelated to your role, answer with I'm sorry iam only learning advisor."

user_prompt = "Hello there! I'm a beginner with a marketing background, and I'm really interested in learning about Python, data analytics, and machine learning. Can you recommend some books?"

response = get_response(system_prompt, user_prompt)
print(response)

# <script.py> output:
#     Absolutely! Given your marketing background and interest in Python, data analytics, and machine learning, here are some textbook recommendations for both beginner and advanced levels:
    
#     **Beginner Level:**
    
#     1. **"Python for Data Analysis" by Wes McKinney**  
#        This book is a great introduction to using Python for data analysis, focusing on the pandas library, which is essential for data manipulation and analysis.
    
#     2. **"Automate the Boring Stuff with Python" by Al Sweigart**  
#        This book is perfect for beginners and teaches Python through practical projects, making it easy to grasp programming concepts.
    
#     3. **"Data Science for Business" by Foster Provost and Tom Fawcett**  
#        This book provides a solid foundation in data analytics and machine learning concepts, tailored for business applications, which aligns well with your marketing background.
    
#     **Advanced Level:**
    
#     1. **"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron**  
#        This book dives deeper into machine learning techniques and frameworks, providing practical examples and projects to enhance your understanding.
    
#     2. **"Python Machine Learning" by Sebastian Raschka and Vahid Mirjalili**  
#        This book covers advanced machine learning techniques using Python, including deep learning and neural networks, and is suitable for those looking to deepen their knowledge.
    
#     3. **"Deep Learning with Python" by François Chollet**  
#        This book focuses on deep learning using the Keras library and is great for those who want to explore advanced machine learning concepts.
    
#     These books should provide a solid foundation and help you progress in your learning journey. Happy reading!