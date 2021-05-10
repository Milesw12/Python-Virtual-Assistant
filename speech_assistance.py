import speech_recognition as sr
import pyttsx3
import pyaudio
import random
engine = pyttsx3.init()



def assistantResponse(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ask something!')
        audio = r.listen(source)

    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print('Google speech recognition could not understand')
    except sr.RequestError as e:
        print("Request error from google speech recognition")
    
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
            

