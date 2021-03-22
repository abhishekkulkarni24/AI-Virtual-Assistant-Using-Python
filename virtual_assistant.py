import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def assistantVoice(audio):
    engine.say(audio)
    engine.runAndWait()

assistantVoice("Hello Boss")