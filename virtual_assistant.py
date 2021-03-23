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

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
           successful
    "error":   `None` if no error occured, otherwise a string containing
           an error message if the API could not be reached or
           speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
           otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        print("Listening ...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    
    try:
        res =    recognizer.recognize_google(audio)
        print(res)
    except sr.RequestError:
        print("error")

    return res

wish()
status = True

recognizer = sr.Recognizer()
microphone = sr.Microphone()


while status:
    query = recognize_speech_from_mic(recognizer,microphone).lower()
    if "what is" in query or "who is" in query:
        assistantVoice("searching in wekipedia")
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences=2)
        print(result)
        assistantVoice(result)
    else:
        pass            