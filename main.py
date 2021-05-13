#Required libaries to use the assistant
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
import sys


#engine set up
#initalising the text to speech engine 
engine = pyttsx3.init()
#configuring the voice (not nessessary but adds more personal touch to allow user to configure to liking.)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id) 

#Set up logging to assist in debugging issues
LogOutput()
#sets the wikipedia library to only output from en.wikipedia.org
wikipedia.set_lang("en")

def assistantResponse(output):
    #neatens code to do two lines in one, reducing any issue from a line being forgotten.
    engine.say(output)
    engine.runAndWait()

def recordAudio():
    #creates a new recogniser instance for running speech to text
    r = sr.Recognizer()
    print("A moment of silence, please...")
    engine.say("A moment of silence, please...")
    engine.runAndWait()
    #configuring the theshhold for speech pickup, ensures background noise doesnt interfere with speech detection.
    with sr.Microphone() as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    engine.say("Set minimum energy threshold to {}".format(round(r.energy_threshold, 2)))
    engine.runAndWait()
    #Speech engine configured and calibrated
    #Awaits user input
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
    #If recogniser is unable to process the audio, the error messages are caught and replaced with a user friendly explaination
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
    #returns the text output from the speech to the function to use further on
    return data

def greetings(text):
    Greeting_Inputs = ['hi', 'hey', 'hola', 'bonjour', 'hello']
    Greeting_Response = ['hi', 'hey', 'hola', 'greetings', 'bonjour', 'hello']

    #refering to line 140, if user says a keyword from greeting_inputs, assistant will return with a response from list Greeting_response
    for word in text.split():
        #ensures the string is lower case to remove capitalisation comparison error
        if word.lower() in Greeting_Inputs:
            return random.choice(Greeting_Response)
    return ''

def wakeWord(text):
    #defined a wake_word to trigger the assistant
    WAKE_WORD = ('computer')

    text = text.lower()

    for phrase in WAKE_WORD:
        #compares user input to the wakeword
        if phrase in text:
            return True
    return False

def getDate():
    #created variable to hold the current date to use to grab the day and month
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th','14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    #builds the string containing the current date using the variables and lists above then returns the String to the function.
    return 'Today is ' + weekday + ', ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1]

def WishMe():
    responses = ''
    #finds the current hour of day in 24h format
    hour = int(datetime.datetime.now().hour)
    #run the hour through a if loop to filter it into a specific output
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

#Calling the formal greeting contained in the function Line 115
WishMe()


while True:
    #assigns the function from line 32 to a variable to enable processign of the function output
    text = recordAudio()
    responses = ''
    #compare text to a list of different reponses set out in a elif loop
    if  text == "assistant":
        responses = responses + greetings(text) #calling function from ln 76

    elif 'date' in text:
        get_date = getDate() # line 99
        responses = responses + ' ' + get_date

    elif text == "who am I" :
        user = getpass.getuser() #this function checks the env variables (logname, user, lname, username) and returns the first string it finds aka current logged on user 
        responses = responses + 'You are ' + user
    
    elif text == "how are you":
        responses = responses + "I'm fine sir"

    elif text == "who are you":
        responses = responses + "I am PiAsst created by Miles"
    
    elif 'Wikipedia' in text: 
        #runs the recordAudio() function again
        print("please say what you want to search for on wikipedia")
        assistantResponse('Please say what you want to search for on wikipedia')
        request = recordAudio()
        #checks if user cancels the request
        if 'cancel' in request:
            #terminates the current loop and resumes execution at the next statement
            break
        else:
            assistantResponse('Searching Wikipedia...please wait')
            #tts the request back to user as it runs
            engine.say(request)
            #searches wikipedia for page named in request
            text = wikipedia.page(request)
            #outputs the page contents and reads back page to user
            print(text.content)
            responses = responses + text.content


    elif 'break' or 'stop' or 'bye' in text:
        #checks if user is saying to stop the assistant
        print("goodbye!")
        assistantResponse("goodbye!")
        #exit the program and come out of the execution process
        sys.exit()

        
        
    
    else: #If input doesnt meet the other criterias, the assistant will apologise for not having the feature.
        responses = responses + "I'm sorry i can't do that yet"

    #after running through loop, these two lines will trigger and output a reponse to the query the user asks.
    assistantResponse(responses)
    print(responses)       

