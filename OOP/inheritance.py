# class User:       # parent class
    
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
    
#     def show_details(self):
#         print(f"Hi I am {self.name}. My id is {self.id}.")
    

# class Student(User):     # child class
#     pass


# s2 = Student("Shyam","S02")
# s1 = Student("Ram","S01")

# s2.show_details()
# s1.show_details()



#init method in child class

class User:         # parent class
    
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
    
    def show_details(self):
        print(f"Hey, My name is {self.name}. My student id is {self.id}. I am {self.age} years old.")
    
    
class Student(User):      #child class
    
    def __init__(self,marks,name,id,age):
        User.__init__(self,name,id,age)
        self.marks = marks
        
    def show_marks(self):
        print(f"I got {self.marks} marks in exam.")
    
s1 = Student(97,"Ram","S001",27)
s1.show_details()
s1.show_marks()

