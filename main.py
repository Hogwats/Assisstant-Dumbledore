#custom package

import datetime
from base.general import  *
from base.activaty import ( sendEmail, wiki, 
                           play_song, time_now, send_mail, conversation,weather )
from base.data import convo
from base.lovecalci import eliminateCommonChars,calculator,result

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import pyaudio
import pywhatkit as py

#pip packages
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('speed',1)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

        speak(" Team ? How Are You  . Ok  . Tell Me How Can I Help You ")

    
    
if __name__ == "__main__":
    wishMe()
    msg = "hello"
    conversation(msg)
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            wiki(query)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music from youtube' in query:
            play_song()
            
        elif 'the time' in query:
            time_now()

        elif 'weather' in query:
        	weather()
        elif  'conversation' in query:
            while True:            
                speak('Lets start conersation')
                conves =  takeconvo().lower()
                convo(conves)
                

        elif  'play on youtube' in query:
            video = ytvideo.lower()
            py.playonyt(video)
        
        elif 'check flames' or ' open love calculator' in query:
            while True:
                result():
        else:
            speak("I Can't Able To Understand What You Are Speaking ")

