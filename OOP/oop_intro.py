""" 
OOP - Object Oriented Programming

Uses:
1. Clean and clear structure
2. Reuse of codes.
3. Easy to maintain, easy to debug, 
4. DRY concept(Dont Repeat Yourself)
5. Application Development

Class - It is a collection of objects,methods, similar datas.

Object - It is used to access and manipulate the properties,logic,methods,etc of class.

Note: We can not directly access the properties of class. We need to create an object to access the properties of class.

Characteristics of OOP:

1. Inheritance - to implement the properties of parent class to its child classes

2. Encapsulation - the binding of data and methods, process of hiding the data and methods.

3. Abstraction - giving the access of only required/essential data to users,  hiding the implementation details of data

4. Polymorphism - single interface, but many implementations,   same method but behaves differently

5. Reusability - created once, but can be reused accross the multiple platforms/programs

6. Message Passing - parameters, objects

"""


class show_details:
    
    name = "ram"
    
    def show(self):
        print("square.")
        
    def show(self):
        print("cube")
obj1 = show_details()
print(obj1.name)
obj1.show()


# init method
# self parameter
# multiple parameter
# properties
# accessing the properties using the self parameter