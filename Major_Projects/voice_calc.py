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
from tkinter import *
from tkinter import scrolledtext, ttk


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
    
    operators = [word for word in command if word in ["+","-","/","*"]]  
    if len(operators) > 1:
        result = "Unsupported Operation"
        print("Unsupported opetaion")
        return result
    
    else:
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
                
            elif "square root" in command :
                
                numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
                result = math.sqrt(numbers)
            
            elif "square" in command :
                
                numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
                result = numbers[0] ** 2
                
            elif "cube root" in command :
                
                numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
                result = numbers[0] ** 1/3
                
            elif "cube" in command :
                
                numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
                result = numbers[0] ** 3
                
            elif "even" in command or "odd" in command :
                
                numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
                if numbers[0] % 2 == 0:
                    result = "Even"
                else:
                    result = "Odd"
                
            elif "prime" in command or "composite" in command :
                
                numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
                
                if numbers[0] == 1:
                    result = "Neither prime or composite"
                else:
                    is_prime = True
                    for i in range(2,numbers[0]):
                        if numbers[0] % i == 0:
                            is_prime = False
                    if is_prime == True:
                        result = "Prime"
                    else:
                        result = "Composite"
                            
            elif "hcf" in command or "highest common factor" in command :
                
                numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
                result = math.gcd(numbers[0],numbers[1])
                        
            elif "lcm" in command or "lowest common multiple" in command :
                
                numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
                result = (numbers[0] * numbers[1]) // math.gcd(numbers[0],numbers[1])
                
            elif "percent" in command or "percentage" in command or "%" in command :
                
                numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
                
                percentage = numbers[0]
                total = numbers[1]
                result = (percentage/100) * total
                
            
            elif "log" in command or "logarithm" in command :
                
                numbers = [float(n) for n in command.split() if n.replace('.',"",1).isdigit() ]
                
                if "base" in command and len(numbers) == 2:
                    result = math.log(numbers[0],numbers[1])
                else:
                    result = math.log10(numbers[0])
            else:
                speak("Unsupported operation")
                result = "Unsupported operation"
            
            
        except Exception:
            print("Error")
            result = "Error"
        
        return result
            
        
def start_listening():
    pass
    # this function implements multi-threading, it executes "listen1" function in separate thread
    
def stop_listening():
    global stop_listening
    stop_listening = True
    # UI logic- it show the message of listening stopped in ui
        
def clear_conversation():
    pass
    # UI logic - it erase all the contents of conversation box
                        
            
root = Tk()
root.title("VOice Calculator")
root.geometry("700x500")
root.resizable(False,False)
root.configure(bg="#E7F6F6")


style = ttk.Style()
style.theme_use("calm")
style.configure("TButton" ,font = ("Arial",10,"bold"), background = "#008000" , foreground = "BLACK", padding = 10)
style.map("TButton",background = [("active","#FFA500")])
style.configure("TLabel", background = "CYAN", foreground = "BLACK",font = ("Arial",10,"bold") )
style.configure("TScrolledText", background = "WHITE", foreground = "BLACK",font = ("Arial",10,"bold"), padding = 10)


# BUtton  1

# BUtton 2

# BUtton 3

# Label
