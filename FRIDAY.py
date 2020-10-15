##########################################################################################################
# Initial Imports needed to create voice chat bot
###########################################################################################################
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

import tkinter

# from tkinter import all
from tkinter import *

from PIL import ImageTk,Image


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

##########################################################################################################
# Import all your needed files/functions into this main program, FRIDAY.py
###########################################################################################################

from introduction import intro
from general_response import gen_response

##########################################
# initialize recognizer
# responsible for recognizing speech 
##########################################
r = sr.Recognizer()

##########################################
# function to record audio
##########################################
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


###############################################################################################################
# this will be friday's playsound function; uses a temp saved audio file and then deletes it upon 'exit' command 
################################################################################################################
def friday(audio_string):
    tts = gTTS(text=audio_string, lang='en') 
    r = random.randint(1, 10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

##########################################################################################################
# create initial screen for chat bot 
###########################################################################################################

# create variable of value tkinter to implement initial screen
app=Tk()
#screen title
app.title("Friday Chat Bot")
#set width and height of screen 
screen = Canvas(app,width=926,height=720)
# set image of screen
image=ImageTk.PhotoImage(Image.open("friday.png"))
screen.create_image(0,0,anchor=NW,image=image)
screen.pack()
app.mainloop()

##########################################################################################################
# Initial script when chat bot program is running
###########################################################################################################

#friday('Hello! Are you a male or a female?')
#friday('If you are a male, please respond to me and say: I am a dude. If you are a woman, please respond to me and say: I am a woman. Also, ')
#friday('If you do not want to label yourself and decline to answer, then please respond to me and say: I decline to answer. So, ')
friday('which one do you consider yourself as?')

#now, we are creating a while loop to continuously have computer listen to what I am saying
time.sleep(1) #waits however many seconds we want

#while loop to allow program to continue to listen to user and respond + records and deletes audio once finished
while 1:
    user_response = record_audio()
    intro(user_response)
    gen_response(user_response)

