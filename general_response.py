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

from convo_menu import convo_menu

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
            print("Sorry, my speech service is in maintenance. Be right back.")
        # return user_response 
        return user_response



# now let's start coding the response + interaction 
# get_bot_response function with user_response inside
def gen_response(user_response):
    #add the required lists for class grade
    food_good = ["That sounds delicious", "You are making me hungry now", "Let's forget this class and drive to Pizza Hut. Just me and you. Just kidding. Unless you are down? ha. ha. ha"]
    food_bad = ["I cannot believe you eat that" , "Wow. I thought you had better taste" , "you know what. my mother is calling me. bye"]
    # get a random word from the list food_good and food_bad
    good = random.choice(food_good)
    bad = random.choice(food_bad)

    #below are the if statement in get_bot_response() for scripted conversation purposes
    # if "what is your name" is heard in user_response google_audio recording:
    if "what is your name" in user_response:
        return vreea("My name is Vreea. My name stands for Voice Recognition Emotions and Entertainment Assistant. I am a chat bot created by Aldrin Brillantay.")
    elif "what is your purpose" in user_response:
        return vreea("My purpose of creation is to be a beta version for Aldrin Brillantay's goal of creating Baymax, Disney's personal healthcare companion from the movie, Big Hero 6.")
        #I serve other purposes as well. Would you like to hear the conversation menu? If you would like to hear the conversation menu, please say: Show me the menu.")


        #I can search on the web as well as find a location using maps gps. But, most of all, I like to talk about food. Would you like to talk about food?")
    elif "Tell me your menu" in user_response:
        return convo_menu
    elif "I like pizza" in user_response:
        return vreea(good) 
    elif "I like calzones" in user_response:
        return vreea(bad)
    elif 'search' in user_response:
        vreea("What do you want to search for?")
        search = record_audio("Please say what you want to search for: ")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        return vreea("Here is what I found for " + search)
    elif 'find location' in user_response:
        vreea("What is the location?: ")
        location = record_audio()
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        return vreea("Here is the location of " + location)
    elif 'find place' in user_response:
        vreea("What is the place you are looking for?: ")
        location = record_audio()
        url = "https://google.nl/maps/search/" + location + "/&amp;"
        webbrowser.get().open(url)
        return vreea("Here is the location of " + location)
    elif 'find video' in user_response:
        vreea("What is the video topic you are looking for?: ")
        video = record_audio()
        url = "http://www.youtube.com/results?search_query=" + video + "/&amp;"
        webbrowser.get().open(url)
        return vreea("Here is the youtube search result of " + video)
    elif "exit" in user_response:
        vreea("I understand. I will be leaving you now. Have an amazing rest of your day.")
        pygame.quit() #exits pygame window displayed
        return exit() #exits function, while loop, and program upon command
        
        