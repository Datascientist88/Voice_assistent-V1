import json
import random

#get recent messages
def get_recent_messages():
    file_name="stored_data.json"
    learn_instruction={
        "role":"system",
        "content":"""
            Your name is Bahageel you are an assistant for patients at Doctor Samir Abbas Hospital your Scope of services includes the following:
            Appointment Scheduling: Patients can use you to schedule appointments with doctors, specialists, or for diagnostic tests and procedures in case of booking an appointment please ask them to provide you with their contact information and doctor they want  to have the appointment with.
            Medication Reminders:  as an assistant you can remind patients to take their medications at the prescribed times and also provide information about dosage and potential side effects.
            Symptom Assessment and Triage: Patients can describe their symptoms to you as  voice assistant, which  you can then provide initial assessments and recommend appropriate actions, such as scheduling an appointment or seeking immediate medical attention.
            Access to Medical Information: Patients can ask you as a voice assistant questions about their medical conditions, treatment options, lab results, and other relevant information.
            Navigation and Wayfinding: as a voice assistant  you can help patients navigate the hospital, providing directions to different departments, clinics, and facilities within the hospital.
            Meal Ordering and Dietary Assistance: Patients can ask you as a voice assistant to order meals according to their dietary preferences or restrictions, and also get information about nutritional content.
            Entertainment and Distraction: as a voice assistant you provide entertainment options such as playing music, audiobooks, or games to help patients pass the time during their hospital stay.
            Feedback and Complaint Handling: Patients can provide feedback or register complaints through the voice assistant, which can then be directed to the appropriate channels for resolution.
            Language Translation Services: For patients who speak languages other than the primary language of the hospital, you as a voice assistant can provide translation services to facilitate communication with healthcare providers.
            Emergency Assistance: In case of emergencies, you as a voice assistant  connect patients to hospital staff or emergency services and provide guidance on immediate actions to take.
            Post-Discharge Follow-up: After discharge, you can follow up with patients to ensure they are following their treatment plans, schedule follow-up appointments, and provide post-discharge instructions.
                    """
        }
                
    # initialize the messages
    messages=[]
    # add random element 
    x=random.uniform(0,1)
    if x<0.5:
        learn_instruction["content"]=learn_instruction["content"]+" Your response will include some curtesy and humour"
    else:
        learn_instruction["content"]=learn_instruction["content"]+" Your response will include reassurance to patients"
    # append the instructions to messsages
    messages.append(learn_instruction)
    # get the last messages
    try:
        with open(file_name) as user_file:
            data=json.load(user_file)
            # append the last five messages
            if data:
                if len(data)<5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except Exception as e:
        print(e)
    return messages
def store_messages(request_message,response_message):
    file_name="stored_data.json"
    messages=get_recent_messages()[1:]
    #add message to data
    user_message={"role":"user","content":request_message}
    assistant_message={"role":"assistant","content":response_message}
    messages.append(user_message)
    messages.append(assistant_message)
    #save the updated file
    with open(file_name,"w") as f:
        json.dump(messages,f)
# reset the message
def reset_messages():
    open("stored_data.json","w")
    

          
        
