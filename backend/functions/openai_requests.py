import openai
import os 
from decouple import config
from functions.database import get_recent_messages
from dotenv import load_dotenv
# retrieve our environment variables
load_dotenv()
openai.organization=os.getenv("OPENAI_ORG")
openai.api_key=os.getenv("OPENAI_API_KEY")

#openai whisper

# convert audio to text 
def convert_audio_to_text(audio_file):
    try:
        transcript=openai.Audio.transcribe("whisper-1",audio_file)
        message_text=transcript["text"]
        return message_text
    except Exception as e:
        print(e)
        return 
# Openai Chatgpt
# get response to our messages
def get_chat_response(message_input):
    messages=get_recent_messages()
    user_message={"role":"user","content":message_input}
    messages.append(user_message)
    print(messages)
    try:
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",messages=messages
        )
        message_text=response["choices"][0]["message"]["content"]
        return message_text
    except Exception as e:
        print(e)
        return


     

