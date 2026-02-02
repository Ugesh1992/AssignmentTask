#Module 4
#Task 1: Calculate Factorial Using a Function
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number : "))
result = factorial(num)
print(f"Factorial of {num} is {result}")


#Task 2: Using the Math Module for Calculations
import math

num = int(input("Enter a number : "))
sqrt = math.sqrt(num)
log = math.log(num)
sine = math.sin(num)
print(f" Square root of {num} is : {sqrt}")
print(f" Logarithm  of {num} is : {log}")
print(f" Sine  of {num} is : {sine}")
