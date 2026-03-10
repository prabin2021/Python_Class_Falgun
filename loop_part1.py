""" 
Loop statements:
if we need to perform any repetative task then we can use loop statements.

We have two types of loop statements in python:

1. for loop - we can use for loops when we are known about the number of iterations.

2. while loop - we can use while loops when we are not known about the number of iterations.

"""

# name = ["ram", "shyam", "hari", "gita"]
# print(name[1])
# for i in name:
#     print(i)



# subject = "Hello Python"
# print(subject)
# for i in subject :
#     print(i)


# for i in range(5,11):
#     print(i)
    
# for i in range(5,11):
#     print("Ram")


# for i in range(1,11,3):
#     print(i)

# for i in range(1,11,3):
#     print("Shyam")



# for i in range(1,5):
#     print(i)

# sum = 0
# for i in range(1,5):
#     sum = sum + i
# print(sum)


for i in range(5):  # 5 times  0,1,2,3,4
    for j in range(3):  # 3 times   0,1,2
        print("1", end="")
    print("\n")
    

for i in range(5): # 0,1,2,3,4
    for j in range(i): 
        print("*", end="")   
    print("\n")