import os
import re
import sqlite3
#import text2emotion as te
import webbrowser
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
from hugchat import hugchat

conn = sqlite3.connect("debbie.db")
cursor = conn.cursor()
#greet
@eel.expose
def greet():
    speak("Hello I am Debbie")

#click sound for mic button

@eel.expose
def playClickSound():
    music_dir = "www\\assets\\audio\\click_sound.mp3"
    playsound(music_dir)
 

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "").strip().lower()

    if query != "":
        try:
            # Try to find the application in sys_command table
            cursor.execute('SELECT path FROM sys_command WHERE LOWER(name) = ?', (query,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])
                return

            # If not found, try to find the URL in web_command table
            cursor.execute('SELECT url FROM web_command WHERE LOWER(name) = ?', (query,))
            results = cursor.fetchall()
            
            if len(results) != 0:
                speak("Opening " + query)
                webbrowser.open(results[0][0])
                return

            # If still not found, try to open using os.system
            speak("Opening " + query)
            try:
                os.system('start ' + query)
            except Exception as e:
                speak(f"Unable to open {query}. Error: {str(e)}")

        except Exception as e:
            speak(f"Something went wrong: {str(e)}")



def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Sorry, I couldn't find what to play on YouTube.")


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response

def chatbot_response(query):
    query = query.lower()
    res=""
    
    if 'hello' in query:
        res="Hi there! How can I help you today?"
        speak(res)
    elif 'how are you' in query:
        res="I'm doing well, thank you! How about you?"
        speak(res)
    elif 'what is your name' in query:
        res="I am your voice assistant. You can call me Assistant."
        speak(res)
    else:
        speak("I'm sorry, I don't understand that. Could you please rephrase?")
        
# Emotion detection function using text2emotion
#def detect_emotion(query):
#    emotions = te.get_emotion(query)  # Detect emotions from the text
#    dominant_emotion = max(emotions, key=emotions.get)  # Get the emotion with the highest score
#    return dominant_emotion, emotions
#
#def disp_emotion(query):
#    emotion, emotions = detect_emotion(query)
#    print(f"Detected Emotion: {emotion}")
#    #eel.DisplayMessage(f"Detected Emotion: {emotion}")  # Show the detected emotion on frontend
#    if emotion == 'happy':
#        speak("I'm glad you're happy!")
#    elif emotion == 'sad':
#        speak("I'm sorry you're feeling sad. How can I help?")
#    elif emotion == 'angry':
#        speak("I sense some anger. Let's calm down and talk.")
#    elif emotion == 'surprise':
#        speak("It sounds like you're surprised!")
#    elif emotion == 'fear':
#        speak("Don't worry, everything is fine. I'm here to help.")


from datetime import datetime
# Insert new appointment into the database 
def add_appointment(title, date, time, description):
    conn = sqlite3.connect('debbie.db')
    c = conn.cursor()
    c.execute("INSERT INTO appointments (title, date, time, description) VALUES (?, ?, ?, ?)",
              (title, date, time, description))
    conn.commit()
    conn.close()
    print("Appointment added successfully.")

# Retrieve all appointments
def view_appointments():
    conn = sqlite3.connect('debbie.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM appointments ORDER BY date, time")
    appointments = c.fetchall()
    conn.close()
    if appointments:
        for appointment in appointments:
            print(f"Title: {appointment[1]}. Date: {appointment[2]}. Time: {appointment[3]}. Description: {appointment[4]}")
            speak(f"Title: {appointment[1]}. Date: {appointment[2]}. Time: {appointment[3]}. Description: {appointment[4]}")
            eel.DisplayMessage(f"Title: {appointment[1]}. Date: {appointment[2]}. Time: {appointment[3]}. Description: {appointment[4]}")
            
    else:
        speak("No appointments found.")