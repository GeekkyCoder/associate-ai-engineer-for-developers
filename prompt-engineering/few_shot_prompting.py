# Sentiment analysis with few-shot prompting
# You're working on market research and your goal is to use few-shot prompting to perform sentiment analysis on customer reviews. You are assigning a number for a given customers conversation: -1 if the sentiment is negative, 1 if positive. You provide the following examples as previous conversations for the model to learn from.

# The product quality exceeded my expectations -> 1
# I had a terrible experience with this product's customer service -> -1


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  model = "gpt-4o-mini",
  # Provide the examples as previous conversations
  messages = [{"role": "user", "content": "The product quality exceeded my expectations"},
              {"role": "assistant", "content": "1"},
              {"role": "user", "content": "I had a terrible experience with this product's customer service"},
              {"role": "assistant", "content": "-1"},
              # Provide the text for the model to classify
              {"role": "user", "content": "The price of the product is really fair given its features"}
             ],
  temperature = 0
)
print(response.choices[0].message.content)