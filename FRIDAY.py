#import pygame #look at like 141
#import game
#from game import runGame
from introduction import intro

import os
from os import system #this is a core python package

import random #you want to randomly generate a file name for the audio file

#make sure to have python 3 interpreter ctrl+shift+P 
#pip3 install speechrecognition
#this is google's library performing speech recog API
import speech_recognition as sr

#python time() and datetime() methods for current
import time
import datetime


# pip3 install pyaudio
# installs required pyaudio which is 
# needed to use the microphone
import pyaudio

# import webbrowser package 
import webbrowser


# pip3 install gTTS : use google text to speech interface; whatever we pass in as text, it will create an audio file to speak
from gtts import gTTS

# pip3 install playsound : make sure to also use another package called 'playsound.' If we don't use this, itll open up your defauly sound/audio player to respond... and we don't want that.
import playsound

# pip3 install pyobjc : this has app kit that playsound depends on. PyObjC is a bridge between Python and Objective-C. 
import PyObjCTools 


# initialize recognizer
# responsible for recognizing speech 
r = sr.Recognizer()


#create function to record audio
def record_audio(ask=False): #setting optional ask argument to False
    with sr.Microphone() as source:
        #create if statement for ask argument
        if ask:
            print(ask)
        # create audio variable and set to recognizer object and then use listen() method. Pass in source which is our microphone
        audio = r.listen(source, phrase_time_limit=3) 

        # create variable for user_response and initialize 
        user_response = ''
        # create try block with 2 exceptions
        try:
            #create variable for voice data; whatever we say, we want to put that into a variable. Use recognize_google and pass in our audio variable
            user_response = r.recognize_google(audio)
        # create unknownValueError exception for when it doesn't understand what user is saying
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        # create request error exception if something is wrong/if server isn't working
        except sr.RequestError:
            print("Sorry, my speech service is in maintenance. Be right back.")
        # return user_response 
        return user_response

#this while be friday's(jarvis') function; uses a temp saved audio file and then deletes it upon 'exit' command 
def friday(audio_string):
    tts = gTTS(text=audio_string, lang='en') 
    r = random.randint(1, 10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

# now let's start coding the response + interaction 
# get_bot_response function with user_response inside
def get_bot_response(user_response):
    #add the required lists for class grade
    food_good = ["That sounds delicious", "You are making me hungry now", "Let's forget this class and drive to Pizza Hut. Just me and you. Just kidding. Unless you are down? ha. ha. ha"]
    food_bad = ["I cannot believe you eat that" , "Wow. I thought you had better taste" , "you know what. my mother is calling me. bye"]
    # get a random word from the list food_good and food_bad
    good = random.choice(food_good)
    bad = random.choice(food_bad)

    #below are the if statement in get_bot_response() for scripted conversation purposes
    # if "what is your name" is heard in user_response google_audio recording:
    if "what is your name" in user_response:
        return friday("My name is Friday. I am a chat bot created by Aldrin Brillantay.")
    elif "what is your purpose" in user_response:
        return friday("My purpose of creation is to give Aldrin Brillantay a good grade in school. I serve other purposes as well. I can search on the web as well as find a location using maps gps. But, most of all, I like to talk about food. Would you like to talk about food?")
    elif "I would love to talk about food" in user_response:
        return friday("Okay great! What do you like better? Pizza or Calzones?")
    elif "I like pizza" in user_response:
        return friday(good) 
    elif "I like calzones" in user_response:
        return friday(bad)
    elif 'search' in user_response:
        friday("What do you want to search for?")
        search = record_audio("Please say what you want to search for: ")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        return friday("Here is what I found for " + search)
    elif 'find location' in user_response:
        location = record_audio("What is the location?: ")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        return friday("Here is the location of " + location)
    elif 'find place' in user_response:
        location = record_audio("What is the location?: ")
        url = "https://google.nl/maps/search/" + location + "/&amp;"
        webbrowser.get().open(url)
        return friday("Here is the location of " + location)
    elif "exit" in user_response:
        friday("I understand. I will be leaving you now. Have an amazing rest of your day.")
        return exit() #exits function, while loop, and program upon command



# below is the beginning of what user will initially hear when you run the program
friday('Hello! Are you a male or a female?')
friday('If you are a male, please respond to me and say: I am a dude. If you are a woman, please respond to me and say: I am a woman. Also, ')
friday('If you do not want to label yourself and decline to answer, then please respond to me and say: I decline to answer. So, which one do you consider yourself as?')
#friday("How may I help you today? Now, you can simply speak your requests to me and I shall respond!")
#friday("So, how may I help you?")

#now, we are creating a while loop to continuously have computer listen to what I am saying
time.sleep(1) #waits however many seconds we want

#while loop to allow program to continue to listen to user and respond + records and deletes audio once finished
while 1:
    user_response = record_audio()
    intro(user_response)
    get_bot_response(user_response)

