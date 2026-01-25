"""print(max(1,2,3,4,5,6))
print(min(1,2,3,4,5,6))
str1 ="Education"
print(str1)
print(str1[2:7:3])
"""

name = "Yogesh"
age = 32
# Yogesh is 32 years old
# print(name ,"is", age,"years old")

# using f-string
# print(f"{name} is {age} years old")

#s1 =("Python")
#print(s1 * 3)
"""s1 = "We are learning Python. Python is very effective language"
s2="y"
print(s1.count(s2))"""

student = ["Yogesh",23,100]
print(type(student))
print(student)
print(student[1])
student.extend(("Delhi","India"))
print(student)

fruits = ["Apple","Mango","Banana","Grapes","Mango"]
print(fruits)
fruits.remove("Mango")
print(fruits)

# Tupple
t=("Ram",2,3,4,["Shyam",20,20],("Raja Ram",50))
t2=12,3,4,5,"Om"
print(t2)
print(type(t2))

# Dictionary
groceries ={'milk': 60, 'biscuits': 5 ,'rice': 2}
groceries['eggs']=100
print(groceries)
print(groceries.get('eggss',2222))





num = int(input("Enter a Number : "))
# true-expression if condition else false-expression
print("Even") if num % 2 == 0 else print("Odd")


scores=[2,4,56,78,34,122,654,45]
high = max(scores)
print(f"Highest score is : {high}")