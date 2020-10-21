##########################################################################################################
# imports needed
###########################################################################################################
import datetime
import random
import os
from os import system
from gtts import gTTS
import playsound

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
# this is the function that runs when user responds "I am a dude"
###########################################################################################################
def male():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        vreea("Good morning sir!")
        vreea("How may I help you today? Now, you can simply speak your requests to me and I shall respond! If you would like to hear my conversation menu, simply say: program menu.")
        return vreea("So, how may I help you?")
    elif hour>= 12 and hour < 18:
        vreea("Good afternoon sir!")
        vreea("How may I help you today? Now, you can simply speak your requests to me and I shall respond! If you would like to hear my conversation menu, simply say: program menu.")
        return vreea("So, how may I help you?")
    else:
        vreea("Good evening sir!")
        vreea("How may I help you today? Now, you can simply speak your requests to me and I shall respond! If you would like to hear my conversation menu, simply say: program menu.")
        return vreea("So, how may I help you?")



##########################################################################################################
# this is the function that runs when user responds "I am a woman" during initial introduction
###########################################################################################################
def female():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        vreea("Good morning madam!")
        vreea("How may I help you today? Now, you can simply speak your requests to me and I shall respond! If you would like to hear my conversation menu, simply say: program menu.")
        return vreea("So, how may I help you?")
    elif hour>= 12 and hour < 18:
        vreea("Good afternoon madam!")
        vreea("How may I help you today? Now, you can simply speak your requests to me and I shall respond! If you would like to hear my conversation menu, simply say: program menu.")
        return vreea("So, how may I help you?")
    else:
        vreea("Good evening madam!")
        vreea("How may I help you today? Now, you can simply speak your requests to me and I shall respond! If you would like to hear my conversation menu, simply say: program menu.")
        return vreea("So, how may I help you?")



##########################################################################################################
# this is the function that runs when user responds "I decline to answer"
###########################################################################################################
def decline_to_answer():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        vreea("Okay then. Well, good morning to you, you beautiful human being!")
        vreea("How may I help you today? Now, you can simply speak your requests to me and I shall respond! If you would like to hear my conversation menu, simply say: program menu.")
        return vreea("So, how may I help you?")
    elif hour>= 12 and hour < 18:
        vreea("Okay then. Well, Good afternoon to you, you beautiful human being!")
        vreea("How may I help you today? Now, you can simply speak your requests to me and I shall respond! If you would like to hear my conversation menu, simply say: program menu.")
        return vreea("So, how may I help you?")
    else:
        vreea("Okay then. Well, Good evening to you, you beautiful human being!")
        vreea("How may I help you today? Now, you can simply speak your requests to me and I shall respond! If you would like to hear my conversation menu, simply say: program menu.")
        return vreea("Okay then. So, how may I help you?")


##########################################################################################################
# introduction function that is called in main file, vreea.py
###########################################################################################################
def intro(user_response):
    if "I am a male" in user_response:
        male()
    elif "I am a female" in user_response:
        female()
    elif "I decline to answer" in user_response: 
        decline_to_answer()