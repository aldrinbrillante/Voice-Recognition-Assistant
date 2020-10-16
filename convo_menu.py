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

#make sure to have python 3 interpreter ctrl+shift+P 
#pip3 install speechrecognition
#this is google's library performing speech recog API
import speech_recognition as sr


# initialize recognizer
# responsible for recognizing speech 
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
            print("Sorry, my server is not working at the moment. Trying again...")
        # return user_response 
        return user_response



# now let's start coding the response + interaction 
# get_bot_response function with user_response inside

'''
Insert Coversation Menu via text here: 
"Okay. Let me tell you your options of conversation.
You can also view the Conversation Menu text file on my program as I continue to read you the menu.
I am here for all of your emotional and entertainment needs.
Please wait for me to finish talking before you respond.
You will know that I finished talking once I ask:
'So, how may I help you today?'

Topics of conversation include:

Talking, or venting, about your day.
Discussing your plans for the weekend.
Rating your current emotions from a scale of one to ten. 
Requesting to search the web.
Requesting to find a certain location or place aodjflasdfjasdf.
Requesting to find a Youtube video.


If you would like to vent and complain to me about your day, please sa


emotions: if 1- 5 rate, watch youtube
if 6-10, 

'''
vreea("Okay. Let me tell you your options of conversation")
vreea("Okay test 1 2 3 4 ")