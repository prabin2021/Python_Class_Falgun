"""  
Function:

1. we can resue the codes.
2. we can reduce the length of codes.
3. codes are readable if we use function.
4. function returns the values.

Rules for defining the function name:

1. function name should starts with alphabets or underscore.
2. we can use only digits, alphabets, underscore
3. we can not use predefined function as our function name


"""

# def add(a,b):   # parameters
#     result = a + b
#     return result
    
# final = add(10,6)   # arguments
# print(final)



#Parameters and arguments 

# def even_odd_check(x):  # parameter
    
#     if x % 2 == 0:
#         result = f"{x} is even"
#         return result
#     else:
#         result = f"{x} is odd"
#         return result

# result = even_odd_check(11)  # argument
# print(result)




# Multiple parameters:

# def show_details(name, age, country):
    
#     print(f"Hi, I am {name}. I am {age} years old. I am from {country}.")
    
# show_details("Ram",27,"Nepal")




# Default parameter:

# def show_details(name, country, age=30):   
    
#     print(f"Hi, I am {name}. I am {age} years old. I am from {country}.")
    
# show_details("Ram","India")




# Positional argument and Keyword argument:

# def show_details(name, country, age):   
    
#     print(f"Hi, I am {name}. I am {age} years old. I am from {country}.")
    
# show_details("India","Ram",27)  #positional arguments


# def show_details(name, country, age):   
    
#     print(f"Hi, I am {name}. I am {age} years old. I am from {country}.")
    
# show_details(country = "India",name = "Ram",age = 27) #keyword arguments




# passing dictionary as an argument:

# def show_details(student):
#     print(f"Student name is {student['name']}")
#     print(f"Student id is {student['id']}")
#     print(f"Student marks is {student['marks']}")

# student_dict = {
    
#     "id": "s01",
#     "name":"Ram",
#     "marks": 88
# }

# show_details(student_dict)



# passing list as an argument:

# def show_marks(mark):
#     for i in mark:
#         print(i)

# marks = [34,66,55,78,98,12]

# show_marks(marks)




# Args and Kwargs

# def show_name(*name):  # args = using args to recieve multiple arguments with single variable
#     for i in name:
#         print(i)

# show_name("Ram","shyam","Hari","sita","gita")


# def show_details(**details):    # using kwargs to recieve multiple keyword arguments with single varaible
    
#     print(f"Hi, I am {details['name']}. I am {details['age']} years old. I am from {details['country']}.")
    
# show_details(country = "India",name = "Ram",age = 27) 