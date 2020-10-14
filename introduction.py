
import datetime
import random
import os
from os import system
from gtts import gTTS
import playsound


def friday(audio_string):
    tts = gTTS(text=audio_string, lang='en') 
    r = random.randint(1, 10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

# this is the function that acts when user responds to being 'male' onto terminal
def male():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        return friday("Good morning sir!")
    elif hour>= 12 and hour < 18:
        return friday("Good afternoon sir!")
    else:
        return friday("Good evening sir!")
# this is the function that acts when user responds to being 'female' onto terminal
def female():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        return friday("Good morning madam!")
    elif hour>= 12 and hour < 18:
        return friday("Good afternoon madam!")
    else:
        return friday("Good evening madam!")

def decline_to_answer():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        return friday("Good morning, you beautiful human being!")
    elif hour>= 12 and hour < 18:
        return friday("Good afternoon, you beautiful human being!")
    else:
        return friday("Good evening, you beautiful human being!")

def intro(user_response):
    if "I am a dude" in user_response:
        male()
    elif "I am a woman" in user_response:
        female()
    elif "I decline to answer" in user_response: 
        decline_to_answer()