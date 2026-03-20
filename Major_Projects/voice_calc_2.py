"""
How to run this project:

1. Create a virtual environment:
python -m venv [your_env_name]      (create a virtual environment)
your_env_name\Scripts\activate      (for Windows)
your_env_name/bin/activate          (for MacOS)


2. Install the required libraries
pip install speechrecognition
pip install pyttsx3
pip install threading
pip install tkinter


3. Run the voice_calc.py file
python voice_calc.py

Sample Voice Commands:

1. Add 2 and 2
2. what is the result of 4.0 multiply by 3.0
3. what if 15 is divided by 5
4. is number 16 even or odd
5. what is the result of 3.555 plus 7.9
    #what if 15 is divided by 5  
    #  what if 15 is divided by 5  then add 5 to it.
    #  Add 2 and 2   ->     [add,2,and,2]
    #  what is the result of 35.55 plus 7.9  ->   [what,is,the,result,of,3.5.55,plus,7.9]
    # what is the value of 3 power 4
    # what is the square root of 30
    #check if the number 6 is even or odd
    # what is 30 % of 100

"""

import speech_recognition as sr
import pyttsx3
import threading
from tkinter import *
from tkinter import scrolledtext,ttk
import math

tts_engine = pyttsx3.init()
recognizer = sr.Recognizer()
tts_engine.setProperty("rate",150)


def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()


def listen():
    global stop_listening
    stop_listening = False
    with sr.Microphone() as source:
        while not stop_listening:
            try:
                root.after(0, status_label.config, {'text':"Listening..."})
                audio = recognizer.listen(source,timeout = 7,phrase_time_limit = 5)      # it listens the voice input of user
                command = recognizer.recognize_google(audio)        # it converts the audio data into text data
                status_label.config(text = f"You said: {command}")
                result = calculate(command)
                if result is not None:
                   display_text.insert(END, f"You said: {command}\n")
                   display_text.insert(END, f"Result: {result}\n\n") 
                    
            except sr.WaitTimeoutError:
                print("Time out error")
                status_label.config(text ="Time out error. Please try again.")
            except sr.UnknownValueError:
                print("I didnt understand")
                status_label.config(text ="Sorry, I could not understand. Please try again.")
            except sr.RequestError:
                print("You are offline")
                status_label.config(text ="Sorry, I am unable to process your speech right now. Please check your internet connection.")
                


def calculate(command):
    
    operators = [word    for word in command  if word in ["+","-","*","/"]]
    if len(operators) > 1:
        speak("Multiple operators detected")
        result = "Unsupported operation"
        return result
    
    else:
        command = command.lower()
        try:
            if "add" in command or "+" in command or "plus" in command or "addition" in command or "sum" in command :
                numbers = [ float(n)     for n in command.split()     if  n.replace('.',"",1).isdigit()  ]
                result = sum(numbers)
            
            elif "subtract" in command or "-" in command or "minus" in command :
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                result = numbers[0] - numbers[1]
                
            elif "multiply" in command or "*" in command or "x" in command or "X" in command or "times" in command:
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                result = numbers[0] * numbers[1]
                
            elif "divide" in command or "/" in command or "divided" in command:
               numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
               result = numbers[0]/numbers[1] 
               
            elif "power" in command or "raised to" in command or "exponent" in command:
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                result = math.pow(numbers[0],numbers[1])
            
            elif "sin" in command or "sine" in command:
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                result = math.sin(math.radians(numbers[0]))
               
            elif "cos" in command or "cosine" in command:
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                result = math.cos(math.radians(numbers[0]))
                
            elif "tan" in command or "tangent" in command:
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                result = math.tan(math.radians(numbers[0]))
            
            elif "square root" in command:  
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                result = math.sqrt(numbers[0])
                
            elif "square" in command:
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                result = numbers[0] ** 2
                
            elif "cube root" in command:  
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                result = numbers[0] ** (1/3)
                
            elif "cube" in command:
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                result = numbers[0] ** 3
            
            elif "even" in command or "odd" in command:
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                
                if numbers[0] % 2 == 0 :
                    result = "Even"
                else:
                    result = "Odd"
            
            elif "prime" in command or "composite" in command :
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                if numbers[0] <= 1:
                    result = "Neither prime nor composite"
                else:
                    is_prime = True
                    for i in range(2,numbers[0]):   # start from 2 and go upto 5
                        if numbers[0] % i == 0:
                            is_prime = False
                            break
                    if is_prime:
                        result = "Prime"
                    else:
                        result = "Composite"
                        
            elif "hcf" in command or "highest common factor" in command:
                numbers = [ int(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]   
                result = math.gcd(numbers[0],numbers[1])

            elif "lcm" in command or "lowest common multiple" in command:
                numbers = [ int(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]   
                result = (numbers[0] * numbers[1]) // math.gcd(numbers[0],numbers[1])
                
            elif "percentage" in command or "percent" in command or "%" in command:

                numbers = [float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                if len(numbers) ==2:
                    # percentage = numbers[0]
                    # total = numbers[1]
                    percentage, total = numbers
                    result = (percentage/100) * total
                    
                else:
                    result = "Invalid data"
            
            else:
                speak("Operation not supported")
                result = "Unsupported operation"
                    
        except Exception :
            speak("An error occurred during calculation")
            result = "Error"
    
    speak(f"The result is {result}")
    return result


def start_listening():
    threading.Thread(target=listen).start()
    
def stop_listening():
    global stop_listening
    stop_listening = True
    status_label.config(text ="Listening stopped.")

def clear_conversation():
    display_text.delete(1.0, END)
    status_label.config(text ="Conversation cleared.")


root = Tk()
root.title("Voice Calculator")
root.geometry("700x550")
root.resizable(False,False)
root.configure(bg = "#C1D7ED" )

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font = ("Arial",12,"bold"),background = "#EEEC46",foreground = "BLACK", padding = 10)
style.map("TButton", background = [("active","#D74519")])
style.configure("TLabel", background = "CYAN", foreground = "BLACK", font = ("Arial",12,"bold"))
style.configure("TScrolledText", background = "WHITE", foreground = "BLACK", font = ("Arial",12), padding = 10)        

display_text = scrolledtext.ScrolledText(root, width = 80, height = 20, wrap = WORD, background = "#F5F4E7", foreground = "BLACK", font = ("Arial",12))
display_text.pack(pady = 10)

button_frame = ttk.Frame(root)
button_frame.pack()

start_button = ttk.Button(button_frame, text = "Start Listening", command = start_listening)
start_button.pack(side = LEFT, padx = 10)

start_button = ttk.Button(button_frame, text = "Stop Listening", command = stop_listening)
start_button.pack(side = LEFT, padx = 10)

start_button = ttk.Button(button_frame, text = "Clear Conversation", command = clear_conversation)
start_button.pack(side = LEFT, padx = 10)

status_label = ttk.Label(root, text = "Welcome to Voice Calculator")
status_label.pack(pady = 20)

speak("Welcome to Voice Calculator. Click on Start Listening to begin.")
root.mainloop()