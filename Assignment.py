# Task 1
firstnumber = int(input("Enter the first Number : "))
secondnumber = int(input("Enter the Second Number : "))

print("Addition : " , firstnumber + secondnumber)
print("Subtraction : " , firstnumber - secondnumber)
print("Multiplication : " , firstnumber * secondnumber)
print("Division : " , firstnumber / secondnumber)

# Task 2
firstname = input("Enter your first Name : ")
lastname = input("Enter your last Name : ")
print(f" Hello {firstname} {lastname} !  How are you?")

#Task 1: Check if a Number is Even or Odd
num = int(input("Enter a Number: "))
if num % 2 == 0:
    print(f"{num} is an Even Number")
else:
    print(f"{num} is an Odd Number")


#Task 2: Sum of Integers from 1 to 50 Using a Loop
total = 0
for i in range(1, 50):
     total += i
print(total)