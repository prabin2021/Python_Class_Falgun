""" 
List: ordered, changeable, allows duplicate data to be stored,  syntax- [], 
name = ["ram", "shyam", "hari", "gopal","ram", "sita"]

Tuple: ordered, unchangeable, allows duplicate data to be stored, syntax- (), 
name = ("ram", "shyam", "hari", "gopal","ram", "sita")

Set: unordered, unchangeable, does not allow duplicate data to be stored, syntax- {},
name = {"ram", "shyam", "hari", "gopal", "sita"}

Dictionary: stores data in key-value pair, ordered/unordered, changeable, does not allow duplicate data to be stored, syntax- {},

details = {
    "name": "ram",
    "age": 25,
    "city": "kathmandu"
    }
    
"""

name = ["ram", "shyam", "hari", "gopal","ram", "sita"]


# print(type(name))
# print(name)

# print(name[0])


# name.append("laxman")   #add value at the end of the list

# name.insert(3, "lakshman")  #add value at the specific index

# name.pop()  #remove the last value from the list

# name.remove("ram")  #remove the first occurrence of the value from the list

# print(name.index("hari"))  #return the index of the first occurrence of the value in the list

# name.sort() #sort the list in ascending order
# name.sort(reverse=True) #sort the list in descending order

# name.reverse() #reverse the order of the list

# name.extend(["laxman", "lakshman"]) #add multiple values at the end of the list


print(name)