"""   
JSON - Javascript Object Notation

json library

"""

import json

# student = {
    
#     "id": "S001",
#     "name" : "Ram",
#     "marks": 58
# }

# print(type(student))

# json_format_student = json.dumps(student)  # dumps method change the original format of data into json format
# print(json_format_student)
# print(type(json_format_student))


# student = {
    
#     "id": "S001",
#     "name" : "Ram",
#     "marks": 58
# }

# with open("C:/Users/sigde/OneDrive/Desktop/Python/File_Handling/text.json","w") as f:
#     json.dump(student,f)   # dump method takes two paremeter, first one as which file to dump, second one as where to dump


with open("C:/Users/sigde/OneDrive/Desktop/Python/File_Handling/text.json","r") as f:
    original_student = json.load(f)
print(original_student)
print(type(original_student))

