# car = {
#     "brand": "Toyota",
#     "model": "2025",
#     "color": "red",
#     "price": 5000000
      
# }

# print(car)

# How to access the key or value from the dictionary:

# print(car["brand"])  #access the value using the key


# result = car.get("model")  #access the value using the key using get() method
# print(result)

# result = car.keys()  # return all the keys from the dictionary
# print(result)


# result = car.values()  # return all the values from the dictionary
# print(result)

# result = car.items()  # it counts one key and value pair as one item and return all the items from the dictionary
# print(result)


# car = {
#     "brand": "Toyota",
#     "model": "2025",
#     "color": ["red", "blue", "black"],
#     "price": 5000000
      
# }

# How to change data inside the dictionary:

# car["brand"] = "Tesla"
# print(car)

# car["brand"] = ["Tesla", "Toyota"]
# print(car)

# car["enginetype"] = "petrol"  #add new key and value to the dictionary
# print(car)

# car.update({"enginetype": "petrol"})  #add new key and value to the dictionary using update() method
# print(car)

# How to remove data inside the dictionary:

# car.pop("model")  #remove the key and value from the dictionary using pop() method
# print(car)

# car.popitem()  #remove the last key and value from the dictionary
# print(car)

# car.clear()  #remove all the key and value from the dictionary
# print(car)


# Looping through the dictionary:


# car = {
#     "brand": "Toyota",
#     "model": "2025",
#     "color": ["red", "blue", "black"],
#     "price": 5000000
      
# }

# for i in car:
#     print(i)  # it will return all the keys from the dictionary
    
# for i in car.keys():
#     print(i)  # it will return all the keys from the dictionary

# for i in car:
#     print(car[i])  # it will return all the values from the dictionary using the keys
    
# for i in car.values():
#     print(i)  # it will return all the values from the dictionary
    
    
# for i in car.items():
#     print(i)
    
# for i,j in car.items():
#     print(i,j)


#Nested dictionary:

# cars = {
#     "car1" : { 
#                 "brand": "Toyota",
#                 "model": "2025",
#                 "color": ["red", "blue", "black"],
#                 "price": 5000000
#             },
    
#     "car2" : { 
#                 "brand": "Toyota",
#                 "model": "2025",
#                 "color": ["red", "blue", "black"],
#                 "price": 5000000
#             },
    
#     "car3" : { 
#                 "brand": "Toyota",
#                 "model": "2025",
#                 "color": ["red", "blue", "black"],
#                 "price": 5000000
#             }
# }

# print(cars)

