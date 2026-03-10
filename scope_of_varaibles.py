"""  
Scope of varaible:
LEGB:
 Local Variable: any variables that are defined inside the function
 Enclosing Variable:any variables that are defined in outer function and can be accessed in inner function
 Global variable: any variables that are defined outside the function
 Built-in Variable :

"""

# showing the local and global scope of variable

# name = "ram"

# def show():
#     name = "shyam"
#     print(name)
# show()

# print(name)


# showing the enclosing scope of variable:

# def outer_function():
#     name = "ram"
#     def inner_function():
#         print(name)
#     inner_function()
# outer_function()



# showing the built in scope of variable:

# name = "ram"
# result = len(name)
# print(result)


# Global Keyword:

# name = "ram"

# def show():
#     global name
#     # name = "shyam"
#     print(name)
# show()

# print(name)