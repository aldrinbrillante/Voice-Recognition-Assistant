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
import pygame

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
    #add lists for good/bad talk response
    good_talk = ["Wow. Honestly, it sounded a lot more exciting than my day.", "Wow. What you said was really interesting to hear!", "You seem to be having a good day! That's awesome."]
    bad_talk = ["I cannot believe that happened to you. I'm here if you need anything and I hope you feel better." , "Yikes, that sounds overwhelming. I would recommend you request to search funny cat videos. Regardless, I hope you feel better." , "That sounds like a bad day. I am sorry to hear that and I hope your day gets even a little bit better."]
    # get a random word from the list good_talk and bad_talk
    good = random.choice(good_talk)
    bad = random.choice(bad_talk)

    #below are the if statement in vreea() for scripted conversation purposes
    # if "what is your name" is heard in user_response google_audio recording:
    if "what is your name" in user_response:
        return vreea("My name is Vreea. My name stands for Voice Recognition Emotions and Entertainment Assistant. I am a chat bot created by Aldrin Brillantay. How may I help you?")
    elif "what is your purpose" in user_response:
        return vreea("My purpose of creation is to be a beta version for Aldrin Brillantay's goal of creating a fully functional emotion and entertainment assistant. So, how else may I help you?")
    elif "Vreea, are you listening" is user_response: 
        return vreea("Yes! I am listening to you, and I would love to continue our conversation. How may I help you?")

    elif "program menu" in user_response:
        vreea("Okay. Let me tell you your options of conversation")
        vreea("If you would like to know my name, say: what is your name?")
        vreea("...to know my purpose, say: what is your purpose?")
        vreea("...to tell me about your day, say: Share my day?")
        vreea("...to vent or complain about your day or anything at all, say: Can I complain.")
        vreea("... to search the web, please say: search.")
        vreea("...to find location, please say: find location.")
        vreea("... to find a specific place, please say: find place.")
        vreea("...to find a certain video, please say: find video.")
        vreea("If you have any doubts that I am listening to you, then you can always ask me: Vreea, are you listening?")
        return vreea("So, how may I help you today?")
    
    elif "share my day" in user_response:
        vreea("Of course you can tell me about your day! Please start talking and I will be listening. When you are done talking, pause for 3-5 seconds, and then say: talking complete.")
        return vreea("So, tell me about your day")
    elif "talking complete" in user_response:
        vreea(good)
        return vreea("Happy to have had this conversation with you. If you would like to share about something else, simply say: share my day again. So, how else may I help you?")

    elif "can I complain" in user_response:
        vreea("Of course! You can vent to me about anything! Please start talking and I will be listening. When you are done venting to me, pause for 3-5 seconds, and then say: complaining complete.")
        return vreea("So, what do you want to vent about?")
    elif "complaining complete" in user_response:
        vreea(bad)
        return vreea("Thank you for sharing that to me. It makes me happy to be your friend in this. If you would like to complain about something else, simply say: can I complain again. So, how else may I help you?")

    elif 'search' in user_response:
        vreea("What do you want to search for?")
        search = record_audio("Please say what you want to search for: ")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        vreea("Here is what I found for " + search)
        return vreea("Please let me know if there is anything else I can help you with")
    elif 'find location' in user_response:
        vreea("What is the location?: ")
        location = record_audio()
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        vreea("Here is the location of " + location)
        return vreea("Please let me know if there is anything else I can help you with")
    elif 'find place' in user_response:
        vreea("What is the place you are looking for?: ")
        location = record_audio()
        url = "https://google.nl/maps/search/" + location + "/&amp;"
        webbrowser.get().open(url)
        vreea("Here is the location of " + location)
        return vreea("Please let me know if there is anything else I can help you with")
    elif 'find video' in user_response:
        vreea("What is the video topic you are looking for?: ")
        video = record_audio()
        url = "http://www.youtube.com/results?search_query=" + video + "/&amp;"
        webbrowser.get().open(url)
        vreea("Here is the youtube search result of " + video)
        return vreea("Please let me know if there is anything else I can help you with")
    elif 'play music' in user_response:
        url = "https://www.youtube.com/watch?v=5qap5aO4i9A"
        webbrowser.get().open(url)
        return vreea("Let me know if there is anything else I can help you with")
    elif 'play movies' in user_response:
        url = "https://www.netflix.com/browse"
        webbrowser.get().open(url)
        return vreea("Let me know if there is anything else I can help you with")
    elif 'play game' in user_response:
        return vreea("I apologize. The gaming sector of my program is currently under maintenance. Thank you for your patience. How else can I help you?")
    elif "exit" in user_response:
        vreea("I understand. I will be leaving you now. I wish you an amazing rest of your day.")
        pygame.quit() #exits pygame window displayed
        return exit() #exits function, while loop, and program upon command        
        