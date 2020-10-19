##########################################################################################################
# imports needed
###########################################################################################################
import datetime
import random
import os
from os import system
from gtts import gTTS
import playsound
import webbrowser
import speech_recognition as sr

# initialize recognizer
r = sr.Recognizer()

##########################################################################################################
# vreea(audio_string) function
###########################################################################################################

def vreea(audio_string):
    tts = gTTS(text=audio_string, lang='en') 
    r = random.randint(1, 10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

##########################################################################################################
# Record audio function
###########################################################################################################

def record_audio(ask=False): 
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source, phrase_time_limit=3) 
        user_response = ''
        try:
            user_response = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print("Sorry, my server is not working at the moment. Trying again...")
        return user_response


'''
Insert Coversation Menu via text here: 
"Okay. Let me tell you your options of conversation.
You can also view the Conversation Menu text file on my program as I continue to read you the menu.
I am here for your emotional and entertainment needs.
I ask that you please wait for me to finish talking before you respond.
You will know that I finished talking once I ask:
'So, how may I help you today?'

Topics of conversation include:

Talking, or venting, about your day.
Rating your current emotions from a scale of one to ten. 
Requesting to search the web.
Requesting to find a certain locations or places using Google's GPS software.
Requesting to find a Youtube video.
Playing games for a means of personal entertainment


If you would like to... please say...
1) Tell me about your day: 'Can I tell you about my day?'
2) Vent/Complain: 'I would like to complain'
3) Search the web: 'search'
4) Find location: 'find location'
5) Find place: 'find place'
6) Find video: 'find video'
7) Exit program: 'exit'
'''

def convo_menu():
    vreea("Okay. Let me tell you your options of conversation")
    vreea("Topics of conversation include: talking, or venting about your day, rating your current emotions, searching the web, requesting to find a certain location or place, finding a you tube video, or playing games for the means of entertainment purposes.")
    vreea("Now, if you would like to know my name, just say: what is your name?")
    vreea("If you would like to know my purpose, just say: what is your purpose?")
    vreea("If you would like to: Tell me about your day, please say: Can I tell you about my day?")
    vreea("If you would like to: Vent or complain about your day or anything at all, please say: I would like to complain.")
    vreea("If you would like to search the web, please say: search. In which case, I will ask you what you would you like to search for, and you will respond with the specific topic of your interest.")
    vreea("If you would like to: find location, please say: find location. In which case, I will ask you what specific location you would like me to find, and you should respond back the specific location of your interest.")
    vreea("If you would like to: find a specific place, please say: find place. In which case, I will ask you what specific place you would like me to find, and you should respond back the specific place of your interest.")
    vreea("If you would like to: find a certain video, please say: find video. In which case, I will ask you what video topic you would like me to find, and you should respond back the topic of your interest.")
    
    vreea("If you have any doubts that I am listening to you, then you can always ask me: Vreea, are you listening?")
    
    vreea("So, how may I help you today?")