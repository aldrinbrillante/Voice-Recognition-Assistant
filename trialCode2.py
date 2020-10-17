
import os
from os import system
import random 
import speech_recognition as sr
import time
import datetime
import tkinter
from tkinter import *
from PIL import ImageTk,Image
import pyaudio 
import webbrowser
from gtts import gTTS
import playsound
import PyObjCTools 
from moviepy.editor import VideoFileClip
import pygame
from introduction import intro
from general_response import gen_response

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
# this will be vreea's playsound function; uses a temp saved audio file and then deletes it upon 'exit' command 
################################################################################################################
def vreea(audio_string):
    tts = gTTS(text=audio_string, lang='en') 
    r = random.randint(1, 10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

##########################################################################################################
# create main bot screen for chat bot 
###########################################################################################################

pygame.display.set_caption('VREEA') #Voice Recognition Emotions & Entertainment Assistant
clip = VideoFileClip('vreea.mov')
clip.preview()
pygame.quit()

##########################################################################################################
# Initial script when chat bot program is running
###########################################################################################################


##########################################################################################################
#  extra temp notes:
# while loop 
# while image is open, then vreea 
# incorporate  keeping indow into game loop 
# cowork: inc t2s into game loop of vreea 

# i want the function to work when display is laoded
#############################################################################

#vreea('Hello! Are you a male or a female?')
#vreea('If you are a male, please respond to me and say: I am a dude. If you are a woman, please respond to me and say: I am a woman. Also, ')
#vreea('If you do not want to label yourself and decline to answer, then please respond to me and say: I decline to answer. So, ')
vreea('which one do you consider yourself as?')

#now, we are creating a while loop to continuously have computer listen to what I am saying
time.sleep(1) #waits however many seconds we want

#while loop to allow program to continue to listen to user and respond + records and deletes audio once finished
while 1:
    user_response = record_audio()
    intro(user_response)
    gen_response(user_response)

