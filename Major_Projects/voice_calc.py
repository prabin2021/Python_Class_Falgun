"""
Project - Voice Calculator

Command Samples:

1. What if we add 2 and 5 ?
2. Give me the value of tan 45.5 and sin 30.2.3
3. Subtract 10 from 20.
4. Is number 14 Prime or composite?
5. what is the square of 10?
6. What is 40 % of 500?
7. What will be the value of 4 power 5?

addition
subtraction
divide
product
sin
cos
tan
power


square, square root
cube, cube root
even, odd
prime, composite
hcf, lcm
percentage
pi
log

"""
import pyttsx3
import speech_recognition as sr
import threading
import math


engine = pyttsx3.init()
recognizer = sr.Recognizer()
engine.setProperty('rate',130)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen1():
    
    global stop_listening
    stop_listening = False
    with sr.Microphone() as source :
        while not stop_listening:
            
            try:
                # UI logic - show listening message
                audio = recognizer.listen(source,timeout=5,phrase_time_limit=5)
                command = recognizer.recognize_google(audio)
                # UI logic - show user commands
                result = calculate(command)
                if result is not None:
                    pass
                    # UI logic - display the result in UI
            except sr.WaitTimeoutError:
                print("Time out Error")
                # UI logic - show time out error in ui
            except sr.UnknownValueError:
                print("Sorry, I didnt understand.")
                # UI logic - show the message that the system cannot understand 
            except sr.RequestError:
                print("You are offline.")   
                #UI logic - show the message that your internet connection is unstable              
                
            
def calculate(command):
    
    command = command.lower()
    
    
    try:
        
        if "add" in command or "+" in command or "plus" in command or "addition" in command or "sum" in command : 
            
            numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
            result = sum(numbers)
            
        elif "subtract" in command or "-" in command or "minus" in command or "deduce" in command :
            
            numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
            result = numbers[0] - numbers[1]
        
        elif "multiply" in command or "*" in command or "x" in command or "X" in command or "product" in command or "times" in command: 
            
            numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
            result = numbers[0] * numbers[1]
        
        elif "divide" in command or "/" in command or "divided" in command or "deduce" in command or "quotient" in command :
            
            numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
            result = numbers[0] / numbers[1]
            
        elif "power" in command or "raised to" in command or "exponent" in command :
            
            numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
            result = math.pow(numbers[0],numbers[1])
        
        elif "sin" in command or "sine" in command :
            
            numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
            result = math.sin(math.radians(numbers))
                
        elif "cos" in command or "cosine" in command :
            
            numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
            result = math.cos(math.radians(numbers))
        
        elif "tan" in command or "tangent" in command :
            
            numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
            result = math.tan(math.radians(numbers))
            
            
            
    except Exception:
        print("Error")
            
        
            
        
                        
            
           
    

    