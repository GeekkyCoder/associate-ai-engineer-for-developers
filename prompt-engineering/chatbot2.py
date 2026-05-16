client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the purpose of the chatbot
chatbot_purpose = "You are a customer support chatbot for an e-commerce company specializing in electronics. Your role is to assist users with inquiries, order tracking, and troubleshooting common issues."

# Define audience guidelines
audience_guidelines = "The target audience is tech-savvy individuals interested in purchasing electronic gadgets."

# Define tone guidelines
tone_guidelines = "Use a professional and user-friendly tone while interacting with customers."

# Combine all instructions into the system prompt
system_prompt = chatbot_purpose + " " + audience_guidelines + " " + tone_guidelines

response = get_response(system_prompt, "My new headphones aren't connecting to my device")
print(response)



# <script.py> output:
#     I’m sorry to hear that you’re having trouble connecting your new headphones. Here are a few steps you can try to resolve the issue:
    
#     1. **Check Bluetooth Settings**: Ensure that Bluetooth is enabled on your device. Go to the Bluetooth settings and make sure your headphones are in pairing mode.
    
#     2. **Pairing Mode**: If your headphones have a pairing button, press and hold it until you see a flashing light, indicating they are in pairing mode.
    
#     3. **Forget and Reconnect**: If your headphones were previously connected to your device, try forgetting the device in your Bluetooth settings and then reconnecting.
    
#     4. **Restart Devices**: Sometimes, simply restarting both your headphones and the device you’re trying to connect to can resolve connectivity issues.
    
#     5. **Check Battery Levels**: Ensure that your headphones are charged. Low battery levels can sometimes prevent successful connections.
    
#     6. **Update Firmware**: If applicable, check if there are any firmware updates available for your headphones or your device.
    
#     If you’ve tried these steps and are still having issues, please let me know the make and model of your headphones and the device you’re trying to connect to, and I’ll assist you further!