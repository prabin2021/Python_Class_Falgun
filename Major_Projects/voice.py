"""  
pip install tkinter   - UI

pip install speechrecognition  - compares token audio with words

pip install pyttsx3 - Python text to speech version 3

pip install pyaudio - supportive library for pyttsx3, helps in audio recognizing process


"""

import tkinter
import pyttsx3
import speech_recognition as sr

# engine = pyttsx3.init()
# word = "Hi, I am Prabin Sigdel. I am from Nepal. I am recently teaching python program. My class will end at 9:30 pm."
# engine.say(word)
# engine.runAndWait()


recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate',120)

print("Please speak something")
engine.say("PLease speak something")
engine.runAndWait()

while True:
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source,timeout = 4, phrase_time_limit= 4)
            text = recognizer.recognize_google(audio)
            print(text)
            
        if "exit" in text.lower() or text.lower() == "terminate":
            print("Good Bye")
            # engine.say("I am exiting the system.")
            # engine.runAndWait()
            break
        
    except sr.UnknownValueError:
        print("Sorry, I cannot understand the commands.")
        
    except sr.RequestError:
        print("Sorry, I cannot process the speech.")
            



