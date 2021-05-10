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
    print("A moment of silence, please...")
    with sr.Microphone() as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    with sr.Microphone() as source:

        print('Ask something!')
        audio = r.listen(source)
    data = ''
    try:
        # recognize speech using Google Speech Recognition
        data = r.recognize_google(audio)

        # we need some special handling here to correctly print unicode characters to standard output
        if str is bytes:  # this version of Python uses bytes for strings (Python 2)
            print(u"You said {}".format(data).encode("utf-8"))
        else:  # this version of Python uses unicode for strings (Python 3+)
            print("You said {}".format(data))
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
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
            

