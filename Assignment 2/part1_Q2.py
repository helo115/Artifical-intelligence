# Write a program to find the larger of the two numbers.

num1=int(input("Enter the number 1:"))
num2=int(input("Enter the number 2 :"))

if num1>num2:
    print(num1,"is bigger ")
elif num2>num1:
    print(num2,"is bigger")
else:
    print("both are equal")
