# Write a program to find the largest of the three numbers.

num1=int(input("Enter the number 1:"))
num2=int(input("Enter the number 2:"))
num3=int(input("Enter the number 3 :"))

if num1>num2 and num1>num3:
    print(num1,"is bigger than other ")
elif num2>num1 and num2>num3:
    print(num2,"is bigger than other ")
elif num3>num1 and num3>num2:
    print(num3,"is bigger than other ")
elif num1==num2 and num1>num3:
    print(num1,"is bigger")
elif num1==num2 and num1<num3:
    print(num3,"is bigger")
elif num1==num3 and num1>num2:
    print(num1,"is bigger")
elif num1==num3 and num1<num2:
    print(num2,"is bigger")
elif num2==num3 and num2>num1:
    print(num2,"is bigger ")
elif num2==num3 and num2<num1:
    print(num1,"is bigger")
else:
    print("All are equal")
