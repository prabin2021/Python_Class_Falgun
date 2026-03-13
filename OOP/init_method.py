# init method
# self parameter
# multiple parameter
# properties
# accessing the properties using the self parameter

# self parameter: it helps to recognize the objects(kun object le call gareko bhanera information dinxa) (jun objects le call garxa, tyo object ko properties ko access dinxa)

# class Maths:
#     name = "ram"
    
#     def show(self):
#         print("Hi, I am student")
        
# obj1 = Maths()
# obj1.show()




# class Student:
    
#     "id" = "S001"
#     "name" = "Ram"
#     "marks" = 9
    
#     def __init__(self,id,name,age):       # init method
        
#         self.id = id  #instance
#         self.name = name
#         self.age = age

#     def show(self):
#         print(s1.name)
#         print(s1.age)
        
        
# s1 = Student("s0001","Shyam",18)
# s2 = Student("s0002","Gita",20)
# # s3 = Student()





# class Student:

    
#     def __init__(self,id,name,age):       # init method
        
#         self.id = id  #instance       # yo chai object ko properties ho
#         self.name = name
#         self.age = age

#     def show_details(self):
        
#         print(self.id)
#         print(self.name)
#         print(self.age)
        
#     def show_details2(self):
#         pass
    
#     def show_details3(self):
#         pass
        
        
# s1 = Student("s0001","Shyam",18)
# s2 = Student("s0002","Gita",20)


# # s2.show_details()


class Student:
 
    def __init__(self,id,name,age):       # init method
        
        self.id = id  #instance       # yo chai object ko properties ho
        self.name = name
        self.age = age

    def show_details(self):
        
        print(self.id)
        print(self.name)
        print(self.age)
        
             
s1 = Student("s0001","Shyam",18)       # creation of object

s1.show_details()           # accessing the method using the object

s1.name = "Hari"            # modifying the object properties
s1.contact = 9804859345     # adding the new object properties

s1.show_details()
print(s1.contact)



