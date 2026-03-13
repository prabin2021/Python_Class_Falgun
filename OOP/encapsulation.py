# private property

# class User:
    
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password
    
    
# user1 = User("ram","ram2021")

# print(user1.username)
# print(user1.__password)      # we cannnot access the private property in such way


class User:
    
    def __init__(self,username,password):
        self.username = username
        self.__password = password
    
    def access_private(self):
        print(f"Your username is {self.username}. Your passowrd is {self.__password}")
    

user1 = User("Ram","ram2021")
user1.access_private()