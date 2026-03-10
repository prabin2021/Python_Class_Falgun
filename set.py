name = {"ram", "shyam", "hari", "gopal","ram", "sita"}


# name.append("laxman")   # we cannot add value to the set because it is unchangeable
# name.remove("ram")  # we cannot remove value from the set because it is unchangeable


# name.add("laxman")   #add value to the set

# name.update(["laxman", "lakshman"]) #add multiple values to the set
# name.update({"lakshman", "laxman"}) #add multiple values to the set using another set
# name.update(("lakshman", "laxman")) #add multiple values to the set using tuple


# name.discard("ram")  #remove the value from the set, if the value is not present in the set, it will not give error
# name.clear()  #remove all the values from the set
# del name #delete the set, it will give error if we try to access the set after deleting it
# name.pop() #remove a random value from the set, it will give error if the set is empty

# print(name)


var1 = {1, 2, 3, 4, 5, "ram", "shyam", "sita"}

var2 = {4, 6, 7, 8, "hari", "gopal", "sita", 1}

# Join Operations in set:


#1. Union:

# var3 = var1.union(var2)
# var3 = var1 | var2
# print(var3)


#2. Intersection:

# var3 = var1.intersection(var2)
# var3 = var1 & var2
# print(var3) 


#3. Difference:

# var3 = var1.difference(var2)
# var3 = var2 - var1
# print(var3)

