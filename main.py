import wikipedia
import speech_recognition as sr
import os
from gtts import gTTS #Global text to speech
import datetime
import warnings
import calendar
import random

warnings.filterwarnings('ignore')

def recordAudio():
    r = sr.Recogniser()
    with sr.Microphone() as source:
        print('Ask something!')
        audio = r.listen(source)

    data = ''
    try:
        data = r.recognise_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print('Google speech recognition could not understand')
    except sr.RequestError as e:
        print("Request error from google speech recognition")
    
    return data

def assistantResponse():
    print(text)
    