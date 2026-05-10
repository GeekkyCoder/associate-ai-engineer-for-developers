# Multi-step prompt to plan a trip
# You noticed that the single-step prompt was not effective, because the answer was too vague for what you had in mind. You improve your prompt by specifying the steps to follow for planning. The plan should have four potential locations for your beach vacation, and each location should have some accommodation options, some activities, and an evaluation of the pros and cons.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt detailing steps to plan the trip
prompt = """
create a beach vacation plan for me, 
Step 1:
four potential locations!
Step 2: 
accommodation options, some activities
Step 3: 
 evaluation of the pros and cons.
"""

response = get_response(prompt)
print(response)





# Output:
# Sure! Here’s a beach vacation plan for you:

# ### Step 1: Four Potential Locations

# 1. **Maui, Hawaii**
#    - Known for its stunning beaches, lush landscapes, and vibrant culture.

# 2. **Cancun, Mexico**
#    - Famous for its beautiful resorts, nightlife, and proximity to ancient Mayan ruins.

# 3. **Gold Coast, Australia**
#    - Renowned for its surf beaches, theme parks, and vibrant nightlife.

# 4. **Santorini, Greece**
#    - Celebrated for its breathtaking sunsets, unique architecture, and crystal-clear waters.

# ### Step 2: Accommodation Options and Activities

# #### 1. **Maui, Hawaii**
#    - **Accommodation Options:**
#      - The Ritz-Carlton, Kapalua
#      - Hotel Wailea (adults-only)
#      - Airbnb beachfront condos
#    - **Activities:**
#      - Snorkeling at Molokini Crater
#      - Road to Hana scenic drive