import pyttsx3

def speak_tip(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
