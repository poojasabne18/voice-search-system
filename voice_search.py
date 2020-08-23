import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    #speak("Welcome back")
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    print(Time)
    speak(f"The current time is {Time}")
    
#time()

def wiki(query):
    #query = ("iphone")
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    print(results)
    speak(results)
#wiki()

def takecommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language= 'en-in')
        #print(f"You said:{query}\n")
        if query == "time":
            time()
        else:
            wiki(query)
        
    except Exception as e:
        print(e)
        print("Say that again....")
        speak("Say that again....")
        return "None"
    return query

takecommand()
