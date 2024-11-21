import time
import pyttsx3
import speech_recognition as sr
import eel
import random
from engine.features import *
def speak(text):
    text=str(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    #print(voices)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 125)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=15, phrase_time_limit=6)
    
    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')
        #eel.DisplayMessage('Analyzing Emotion...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}')
        #speak(query)
        time.sleep(2)
        eel.DisplayMessage(query)
        
        

    except Exception as e:
        return ""
    
    return query.lower()

# text = takeCommand()

# speak(text)
@eel.expose
def allCommands(message=1):
    #query = takeCommand()
    #print(query)
    
    if message == 1:
        query = takeCommand()
        print(query)
        #eel.senderText(query)
    else:
        query = message
        #eel.senderText(query)
    try:
        if 'open' in query:
            from engine.features import openCommand
            openCommand(query)
            allCommands()

        elif 'on youtube' in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        elif 'hello' in query:
            from engine.features import chatbot_response
            #disp_emotion(query)
            chatbot_response(query)
            time.sleep(3)
            speak("Is there something else you would like me to do?")
            allCommands()
        
        elif 'add appointment' in query or 'add an appointment' in query or 'schedule an appointment' in query:
            speak("What is the title of the appointment?")
            title = takeCommand()
            speak("When is the appointment?")
            date = takeCommand()
            speak("At what time?")
            time = takeCommand()
            speak("Can you describe what the appointment will be about.")
            description = takeCommand()
            # Add the appointment
            from engine.features import add_appointment
            add_appointment(title, date, time, description)
            speak("Your appointment has been scheduled, Anything else?")
            allCommands()
            
        elif 'tell my appointments' in query:
        # Display all appointments
            from engine.features import view_appointments
            view_appointments()
            speak('Thats all your appointments')  
            allCommands()
        else:
            from engine.features import chatBot
            #disp_emotion(query)
            chatBot(query)
            time.sleep(3)
            speak("Is there something else you would like me to help you with?")
            allCommands()
        if query=='bye':
            eel.ShowHood()
            
    except:
        res=["Pardon I couldn't hear that, can you say that again.","Sorry can you repeat that please.","Say that again please."]
        speak(random.choice(res))
        allCommands()
        #from engine.features import disp_emotion
        #disp_emotion(query)

    

    