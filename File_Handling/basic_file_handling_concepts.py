"""  
File Handling: using python to create, read, write and modify the files.

Main function used in file handling: open()

Opening the files in different modes:

1. "r" : reading mode
2. "w" : write mode
3. "a" : append mode 
4. "x" : create mode


with keyword

os library - 

"""
import os

# f = open("C:/Users/sigde/OneDrive/Desktop/Python/File_Handling/new.txt","r")
# print(f.readline())
# f.close()

# f = open("C:/Users/sigde/OneDrive/Desktop/Python/File_Handling/new.txt","r")
# print(f.read())
# f.close()

# f = open("C:/Users/sigde/OneDrive/Desktop/Python/File_Handling/new.txt","w")
# f.write("Hey, I a  Prabin")
# f.close()

# f = open("C:/Users/sigde/OneDrive/Desktop/Python/File_Handling/new.txt","a")
# f.write("This is python class.")
# f.close()


# with open("C:/Users/sigde/OneDrive/Desktop/Python/File_Handling/new.txt","a") as f:    # opening the file using thw with keyword
#     f.write("I am 24 years old.")

os.remove("C:/Users/sigde/OneDrive/Desktop/Python/File_Handling/new.txt")

