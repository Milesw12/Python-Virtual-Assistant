import speech_recognition as assistance
import pyttsx3
import pyaudio


listener = assistance.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setproperty('voice', voices[1].id)


# with assistance.Microphone() as source:
#    print("Say something: ")
#     audio = listener.listen(source)

def assistantResponse(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

assistantResponse("Hello World")