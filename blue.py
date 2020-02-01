# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 19:12:17 2019

@author: lux-coder
"""

import speech_recognition as sr
import random
import re
import webbrowser

from gtts import gTTS
from datetime import datetime
from pygame import mixer

import openpyxl

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def talk(audio):
    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()

def myCommand():
    #Initialize the recognizer
    #The primary purpose of a Recognizer instance is, of course, to recognize speech. 
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('blue is Ready...')
        r.pause_threshold = 2
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source, duration=1)
        #listens for the user's input
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()
    return command

def blue(command):
    errors=[
        "I don't know what you mean",
        "Did you mean astronaut?",
        "Can you repeat it please?",
    ]
    if 'hello' in command:
        talk('Hello! I am blue. How can I help you?')
        
    elif 'test' in command:
        talk('Test! Test! Test!')
        
    elif 'start primary' in command:
        nowStart = datetime.now()
        print(nowStart)
        dt_stringStart = nowStart.strftime("%H:%M")
        print(dt_stringStart)
        talk('Start time noted @' + dt_stringStart)
        book = openpyxl.load_workbook('timeing.xlsx')
        sheet = book.active
        sheet.append([nowStart])
        book.save('timeing.xlsx')
        
        
        
    elif 'stop primary' in command:
        nowStop = datetime.now()
        print(nowStop)
        dt_stringStop = nowStop.strftime("%H:%M")
        talk('Stop time noted @' + dt_stringStop)
        book = openpyxl.load_workbook('timeing.xlsx')
        sheet = book.active
        sheet.append([nowStop])
        book.save('timeing.xlsx')

    else:
        error = random.choice(errors)
        talk(error)


talk('blue is ready!')

#loop to continue executing multiple commands
while True:
    blue(myCommand())
