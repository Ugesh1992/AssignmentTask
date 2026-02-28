# Task1
student = {"Rajesh" : 59, "Ram" : 40, "Deepak" : 83, "Rahul" : 73}
name = input("Enter the student's Name : ")

if name in student:
    print(f"{name}'s marks are : {student[name]}")
else:
    print("Student is not found")


#Task 2

numlst = list(range(1,11))
resfive = numlst[:5]
revlst = resfive[::-1]

print(f"Original List : {numlst}")
print(f"Extracted first five element : {resfive}")
print(f"Reversed extracted element : {revlst}")
