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
# friday(audio_string) function
###########################################################################################################
def friday(audio_string):
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
        friday("Good morning sir!")
        friday("How may I help you today? Now, you can simply speak your requests to me and I shall respond!")
        return friday("So, how may I help you?")
    elif hour>= 12 and hour < 18:
        friday("Good afternoon sir!")
        friday("How may I help you today? Now, you can simply speak your requests to me and I shall respond!")
        return friday("So, how may I help you?")
    else:
        friday("Good evening sir!")
        friday("How may I help you today? Now, you can simply speak your requests to me and I shall respond!")
        return friday("So, how may I help you?")



##########################################################################################################
# this is the function that runs when user responds "I am a woman" during initial introduction
###########################################################################################################
def female():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        friday("Good morning madam!")
        friday("How may I help you today? Now, you can simply speak your requests to me and I shall respond!")
        return friday("So, how may I help you?")
    elif hour>= 12 and hour < 18:
        friday("Good afternoon madam!")
        friday("How may I help you today? Now, you can simply speak your requests to me and I shall respond!")
        return friday("So, how may I help you?")
    else:
        friday("Good evening madam!")
        friday("How may I help you today? Now, you can simply speak your requests to me and I shall respond!")
        return friday("So, how may I help you?")



##########################################################################################################
# this is the function that runs when user responds "I decline to answer"
###########################################################################################################
def decline_to_answer():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        friday("Okay then. Well, good morning to you, you beautiful human being!")
        friday("How may I help you today? Now, you can simply speak your requests to me and I shall respond!")
        return friday("So, how may I help you?")
    elif hour>= 12 and hour < 18:
        friday("Okay then. Well, Good afternoon to you, you beautiful human being!")
        friday("How may I help you today? Now, you can simply speak your requests to me and I shall respond!")
        return friday("So, how may I help you?")
    else:
        friday("Okay then. Well, Good evening to you, you beautiful human beaing!")
        friday("How may I help you today? Now, you can simply speak your requests to me and I shall respond!")
        return friday("So, how may I help you?")


##########################################################################################################
# introduction function that is called in main file, FRIDAY.py
###########################################################################################################
def intro(user_response):
    if "I am a dude" in user_response:
        male()
    elif "I am a woman" in user_response:
        female()
    elif "I decline to answer" in user_response: 
        decline_to_answer()