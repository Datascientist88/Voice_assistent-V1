# uvicorn main:app --reload
#import the necessary liabraries
from fastapi import FastAPI ,File, UploadFile,HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple  import config
import openai
# custom functions imports
from functions.openai_requests import convert_audio_to_text,get_chat_response
from functions.database import store_messages,reset_messages
from functions.text_to_speech import convert_text_to_speech
#.....
# inialize the app
app=FastAPI()
#CORS
# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:3000",
]
# define CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# check health

# get audio
@app.get("/health")
async def check_health():
    return {"message":"healthy"}

@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message":"conversation reset"}

@app.post("/post-audio/")
async def post_audio(file:UploadFile=File(...)):
    #get saved audio
    #audio_input=open("voice2.mp3","rb")
    # save file from frontend
    with open(file.filename,"wb") as buffer:
        buffer.write(file.file.read())
    audio_input=open(file.filename,"rb")
    #decode audio
    message_decoded=convert_audio_to_text(audio_input)
    if not message_decoded:
        return HTTPException(status_code=400,detail="Failed to decode the audio")
    #get chatgpt response
    chat_response=get_chat_response(message_decoded)
    #handle response exceptions:
    if not chat_response:
        return HTTPException(status_code=400,detail="Failed to get chat response")
    # store messaages
    store_messages(message_decoded,chat_response)
    #convert chat to audio
    audio_output=convert_text_to_speech(chat_response)
    if not audio_output:
        return HTTPException(status_code=400,detail="Failed to get ElevenLabs Audio response")
    # create the generator that yields chunks of audio data
    def iterfile():
        yield audio_output
    # return the audio file 
    return StreamingResponse(iterfile(),media_type="application/octet-stream")


