# local modules
from datetime import date
from datetime import datetime
from model import actions
# from turtle import *

# packages
import webbrowser
import speech_recognition as sr
import pyttsx3
import os

r = sr.Recognizer() 

# config voice recognition
engine = pyttsx3.init()
engine.say(actions.startAppMessage[0])
engine.runAndWait() 

# voice config type
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("ARPA SYSTEM")
    engine.say(actions.startAppMessage[1])
    print("di algo...")
    engine.runAndWait()
    voice = r.listen(source)

    try:
        text = r.recognize_google(voice, language="es-ES")
        print("procesando respuesta...")
        print('dijiste:' + " " + text)

        if "notas" in text:
            os.system("notepad.exe")

        elif "historia de tu nombre" in text:
            engine.say(actions.questions[0])
            engine.runAndWait()       

        elif "spotify" in text or "Spotify" in text:
            os.system("spotify.exe")  

        elif "youtube" in text or "YouTube" in text:
            webbrowser.open_new_tab("https://www.youtube.com")

        elif "fecha" in text or "Fecha" in text:
            engine.say("el dia de hoy es {}".format(date.today()))
            engine.runAndWait()

    except:
        engine.say(actions.startAppMessage[2])
        engine.runAndWait()
        print(":(")