import speech_recognition as sr
import pyttsx3
import pyaudio
import random
from logger import LogOutput
import datetime
import calendar
import getpass
import wikipedia
import webbrowser
import os
from weather import weatherCheck

#engine set up
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id) 
LogOutput()
wikipedia.set_lang("en")

def assistantResponse(output):
    engine.say(output)
    engine.runAndWait()

def recordAudio():
    r = sr.Recognizer()
    print("A moment of silence, please...")
    engine.say("A moment of silence, please...")
    engine.runAndWait()
    with sr.Microphone() as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    engine.say("Set minimum energy threshold to {}".format(round(r.energy_threshold, 2)))
    engine.runAndWait()
    with sr.Microphone() as source:
        print('say something!')
        engine.say("say something")
        engine.runAndWait()
        audio = r.listen(source)
    
    data = ''
    try:
        # recognize speech using Google Speech Recognition
        print("Recognising")
        engine.say("Recognising")
        data = r.recognize_google(audio)

        # we need some special handling here to correctly print unicode characters to standard output
        output = ("You said {}".format(data))
        print(output)
        assistantResponse(output)
    except sr.UnknownValueError:
        output = ("Oops! Didn't catch that, say that again sir.")
        print(output)
        assistantResponse(output)
    except sr.RequestError as e:
        output = ("Uh oh! I Couldn't request results from the Google Speech Recognition service; {0}".format(e))
        print(output)
        assistantResponse(output)
    except KeyboardInterrupt:
        pass
    return data

def greetings(text):
    Greeting_Inputs = ['hi', 'hey', 'hola', 'bonjour', 'hello']
    Greeting_Response = ['hi', 'hey', 'hola', 'greetings', 'bonjour', 'hello']

    for word in text.split():
        if word.lower() in Greeting_Inputs:
            return random.choice(Greeting_Response)
    return ''

def wakeWord(text):
    WAKE_WORD = ('computer')

    text = text.lower()

    for phrase in WAKE_WORD:
        if phrase in text:
            return True
    return False

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th','14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    return 'Today is ' + weekday + ', ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1]

def WishMe():
    responses = ''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        responses = responses +  "Good Morning Sir"
        assistantResponse(responses)

    elif hour>=12 and hour<18:
        responses = responses + "Good afternoon Sir"
        assistantResponse(responses)

    else:
        responses = responses + "Good evening Sir"
        assistantResponse(responses)

    print(responses)


WishMe()

while True:
    text = recordAudio()
    responses = ''
    if  text == "assistant":
        responses = responses + greetings(text)

    elif 'date' in text:
        get_date = getDate()
        responses = responses + ' ' + get_date

    elif text == "who am I" :
        user = getpass.getuser()
        responses = responses + 'You are ' + user
    
    elif text == "how are you":
        responses = responses + "I'm fine sir"

    elif text == "who are you":
        responses = responses + "I am PiAsst created by Miles"
    
    elif 'Wikipedia' in text:
        print("please say what you want to search for on wikipedia")
        assistantResponse('Please say what you want to search for on wikipedia')
        request = recordAudio()
        if 'cancel' in request:
            break
        else:
            assistantResponse('Searching Wikipedia...please wait')
            engine.say(request)
            text = wikipedia.page(request)
            print(text.content)
            responses = responses + text.content


    elif 'weather' in text:
        weatherCheck()
        output = weatherCheck()
        assistantResponse(output)

        
        
    
    else:
        responses = responses + "I'm sorry i can't do that yet" 

    assistantResponse(responses)
    print(responses)       

