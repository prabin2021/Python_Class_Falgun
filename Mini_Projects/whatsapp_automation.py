import pyautogui as py
import time

print("Whatsapp Automation Started")

time.sleep(3)
py.press("win")
time.sleep(1)
py.write("whatsapp")
time.sleep(1)
py.press("enter")
time.sleep(1)
py.hotkey("ctrl","f")
time.sleep(1)
py.write("Python Falgun Shift")
time.sleep(2)
py.press("enter")
time.sleep(2)
assignment = "Assignment: 1. Use the concept of lambda function to calculate any simple logic. 2. Use any standard libraries to automate for any simple process."
py.write(assignment)
time.sleep(2)
py.press("enter")


print("Whatsapp automation completed sucessfully")

