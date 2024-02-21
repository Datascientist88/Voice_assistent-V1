import requests
import os
from dotenv import load_dotenv
load_dotenv()

eleven_labs_api_key=os.getenv("ELEVEN_LABS_API_KEY")

def convert_text_to_speech(message):
    # define body
    body={
        "text":message,
        "voice_settings":{
            "stability":0,
            "similarity_boost":0,

        },
        "model_id": "eleven_multilingual_v2",
    }
    # define voice
    voice_id1="onwK4e9ZLuTAKqWW03F9"
    voice_id= "JBFqnCBsd6RMkjVDRZzb"
    # defining headers
    headers={"xi-api-key":eleven_labs_api_key,"Content-Type":"application/json","accept":"audio/mpeg"}
    endpoint=f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id1}"
    #send request
    try:
        response=requests.post(endpoint,json=body,headers=headers)
    except Exception as e:
        return
    # Handle the response
    if response.status_code==200:
        return response.content
    else:
        return

