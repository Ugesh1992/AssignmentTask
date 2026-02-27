student = {"Rajesh" : 59, "Ram" : 40, "Deepak" : 83, "Rahul" : 73}
name = input("Enter the student's Name : ")

if name in student:
    print(f"{name}'s marks are : {student[name]}")
else:
    print("Student is not found")