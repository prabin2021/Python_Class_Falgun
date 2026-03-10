# Data Structure project
# Mini student management system

student_details = [
    
    # {"std_id":"s01", "std_name":"ram","std_marks": [56,78,76,54,34]},
    # {"std_id":"s02", "std_name":"shyam","std_marks": [56,78,76,54,34]},
    # {"std_id":"s03", "std_name":"bikash","std_marks": [56,78,76,54,34]}
    
]
student_id_list = set()
subject_name = ("Science","English","Maths","Nepali","Social_Studies")

print("Welcome to Student Management system !")
while True:
    
    print("Available Options:\n1. Add Student\n2. View Student\n3. Passed Student\n4. Failed Student\n5. Class Average\n6. Exit")
    
    choice = int(input("Enter your choice:"))
    
    if choice < 1 or choice > 6:
        print("Please enter valid choice.")
        continue
    
    if choice == 1:
        # id = input("Enter student id: ")
        # name = input("Enter student name: ")
        # marks = int(input("Enter student marks: "))
        
        # student = {
            
        #     "std_id": id,
        #     "std_name" : name, 
        #     "std_marks" : marks
        # }
        
        # student_details.append(student)
        # print("Student added sucessfully.")
        
        id = input("Enter student id: ")
        if id in student_id_list:
            print("Student Id already exist.")
            continue
        else:
            student_id_list.add(id)
            name = input("Enter student name:")
            mark_list = []
            for i in subject_name:
                mark = int(input(f"Enter marks for {i}: "))
                mark_list.append(mark)
        
        student = {
            
            "std_id": id,
            "std_name": name,
            "std_marks": mark_list
            
        } 
        student_details.append(student)
        
    elif choice == 2:
        print("\nStudent Details: ")
        print("Id\tName\tMarks")
        for i in student_details:
            print(i["std_id"], "\t", i["std_name"], "\t", i["std_marks"])
            
    elif choice == 3:
        # print("Passed student list:")
        # for i in student_details:
        #     if i["std_marks"] >= 40:
        #         print(i["std_name"])
        
        print("Passed student names")
        for i in student_details:
            count = 0
            for j in i["std_marks"]:
                if j >= 40:
                    count = count + 1
            if count == 5:
               print(i["std_name"]) 
                
                
    elif choice == 4:
        # print("Failed student list:")
        # for i in student_details:
        #     if i["std_marks"] < 40:
        #         print(i["std_name"])
        
        print("Failed student names")
        for i in student_details:
            count = 0
            for j in i["std_marks"]:
                if j >= 40:
                    count = count + 1
            if count != 5:
               print(i["std_name"]) 
    
    elif choice == 5:
        if not student_details:
            print("No data available.")
        else:
            total_marks = 0
            total_subject = 0
            for i in student_details:
                total_marks = total_marks + sum(i["std_marks"])
                total_subject = total_subject + len(i["std_marks"])
                
            average = total_marks/total_subject
            print(f"Average of class is {average}.")
            
                
    elif choice == 6:
        print("Exiting the system")
        break
    
    
# checking the uniqueness of student id
# take input from  user for individual subject marks
# link logic of pass and fail by evaluating each subject marks
# total average of class




