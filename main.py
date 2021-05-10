import speech_recognition as sr
import pyttsx3
import pyaudio
import random
from logger import *


engine = pyttsx3.init()

LogOutput()

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
    engine.say("Set minimum energy threshold to {}".format(round(r.energy_threshold)))
    engine.runAndWait()
    with sr.Microphone() as source:

        print('Ask something!')
        engine.say("Ask something")
        engine.runAndWait()
        audio = r.listen(source)
    data = ''
    try:
        # recognize speech using Google Speech Recognition
        data = r.recognize_google(audio)

        # we need some special handling here to correctly print unicode characters to standard output
        if str is bytes:  # this version of Python uses bytes for strings (Python 2)
            output = (u"You said {}".format(data).encode("utf-8"))
            print(output)
            assistantResponse(output)
        else:  # this version of Python uses unicode for strings (Python 3+)
            output = ("You said {}".format(data))
            print(output)
            assistantResponse(output)
    except sr.UnknownValueError:
        output = ("Oops! Didn't catch that")
        print(output)
        assistantResponse(output)
    except sr.RequestError as e:
        output = ("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
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
    WAKE_WORD = ['Computer']

    text = text.lower()

    for phrase in WAKE_WORD:
        if phrase in text:
            return True
    return False


while True:
    text = recordAudio()
    responses = ''
    if wakeWord(text.lower()) == True:

        try:
            responses = responses + greetings(text)
        except Exception as e:
            responses = responses + ''
            

