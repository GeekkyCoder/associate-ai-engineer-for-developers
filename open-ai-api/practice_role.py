# Adding assistant messages
# Chat models are great for creating conversational applications, but they can be further improved by providing part of a conversation for the model to build on.

# Improve this geography tutor application by including this example student prompt and ideal model response in the messages:

# Example Question: Give me a quick summary of Portugal.
# Example Answer: Portugal is a country in Europe that borders Spain. The capital city is Lisboa.
# Instructions
# 100 XP
# Add the example question and answer provided as a user-assistant pair in the messages sent to the model.
# Example Question: Give me a quick summary of Portugal.
# Example Answer: Portugal is a country in Europe that borders Spain. The capital city is Lisboa.


# Question: How can you add an assistant message to the messages sent to the model?
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add a user and assistant message for in-context learning
    messages=[
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        ____,
        ____,
        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)



#Solution: 
{"role": "assistant", 
 "content": "Japan is an island nation in East Asia known for its advanced technology, rich cultural heritage, and major cities like Tokyo and Kyoto. It has a strong economy, beautiful landscapes including Mount Fuji, and traditions such as sushi, anime, and cherry blossom festivals."
},
{"role": "user", "content": "Give me a quick summary of Japan."}



#More Examples of assistant messages
messages=[
       {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
       {"role": "user", "content": "Give me a quick summary of Portugal."},
       {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
       {"role": "user", "content": "Give me a quick summary of Pakistan"},
       {"role": "assistant", "content": "Pakistan is a country located in south asia,it borders with china,afghanistan, india. it is a nuclear power country, and second most populest muslim country"},
       {"role": "user", "content": "Give me a quick summary of USA?"},
       {"role": "assistant", "content": "USA is a whole gigantic continent, it has many states, newyork is one of them"},
       {"role": "user", "content": "Give ma quick summary of Bangladesh"},
       {"role": "assistant", "content": "Banglasdesh is a country is south asia, borders with Pakistan,India and few others, its capital city is Dhaka"},
       {"role": "user", "content": "Give me a quick summary of Greece."}
   ]