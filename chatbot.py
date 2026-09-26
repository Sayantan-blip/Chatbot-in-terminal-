from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

while True:
    question = input("You: ")
    
    if question.lower() == "exit , quit , stop , end , close , bye , goodbye , see you later , see you soon , see you , talk to you later , talk to you soon , talk to you , catch you later , catch you soon , catch you , farewell , take care , have a good day , have a good night , have a good evening , have a good morning":
        print("Exiting the chat. Goodbye!")
        break
    
    response = client.models.generate_content(
        model="your-model-name",
        contents=question
        
    )
    print("Gemini:", response.text)