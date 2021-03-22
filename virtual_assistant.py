import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def assistantVoice(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        assistantVoice("Good Morning Sir")
    elif hour>=12 and hour<18:
        assistantVoice("Good Afternoon Sir") 
    else:
        assistantVoice("Good Evening Sir")   

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print("user said " + query)
    except Exception as e:
        print(e)
        assistantVoice("Sorry.. Say that again please")   
        return "None"
    return query   

takeCommand()