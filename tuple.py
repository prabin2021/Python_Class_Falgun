name = ("ram", "shyam", "hari", "gopal","ram", "sita")

# print(type(name))


# name.append("laxman")   # we cannot add value to the tuple because it is unchangeable
# name.remove("ram")  # we cannot remove value from the tuple because it is unchangeable


# 1st way to change the data of tuple:
# if we need to manipulate the data of tuple, then we need to change the tuple into list, manipulate the data and then change it back to tuple

# new_name = list(name)
# new_name.append("laxman")   #add value at the end of the list
# name = tuple(new_name)
# print(name)

# new_name = list(name)
# new_name.remove("ram")  #remove the first occurrence of the value from the list
# name = tuple(new_name)
# print(name)



#2nd way to change the data of tuple:
# we can add tuple to another tuple to change the data of tuple

# surname = ("sharma", "thapa", "shrestha", "karki", "sharma", "bhandari")
# name = name + surname
# print(name)



# use of del keyword in tuple:

# del name
# print(name)  # it will give error because the tuple is deleted using del keyword


# Unpacking the tuple:

# surname = ("sharma", "thapa", "bhandari")

# (surname1, surname2, surname3) = surname

# print(surname1)
# print(surname2)
# print(surname3)


 # Unpacking using astrick operator:

# surname = ("sharma", "thapa", "bhandari", "shrestha", "karki")

# (surname1, *surname2, surname3) = surname

# print(surname1)
# print(surname2)
# print(surname3)