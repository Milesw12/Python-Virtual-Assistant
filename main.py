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

    myobj = gTTS(text=text, lang='en', slow=False)

    myobj.save('assistant_response.mp3')

    os.system('start assistant_response.mp3')

def wakeWord(text):
    WAKE_WORDS = ['hey computer', 'okay computer']
    text = text.lower()

    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False


def getDate():
    
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]# e.g. Monday
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'February', 'March', 'April', 'May',
       'June', 'July', 'August', 'September', 'October', 'November',   
       'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', 
                      '7th', '8th', '9th', '10th', '11th', '12th',                      
                      '13th', '14th', '15th', '16th', '17th', 
                      '18th', '19th', '20th', '21st', '22nd', 
                      '23rd', '24th', '25th', '26th', '27th', 
                      '28th', '29th', '30th', '31st']
   
    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'


