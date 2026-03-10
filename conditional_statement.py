""" 
Conditional statement:

if condition: 

else if condition:



else condition: 


Indentation: 4 spaces
indentation is needed on the following areas:
1. conditional statement
2. Loop statement
3. Function 
4. Class

"""

# age = 15

# if age > 18:
#     print("You can vote. if condition is true.")
# elif age == 18:
    
#     print("You can vote")   
# else:
#     print("You can not vote.")
    
    
# Nested conditional statements:


a = int(input("Enter any number:"))

if a >= 0 :
    if a % 2 == 0:
        print(f"{a} is positive even number.")
    else:
        print(f"{a} is positive odd number.")
    
else:  
    print(f"{a} is negative number.")