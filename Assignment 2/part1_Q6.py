#6. Write a program to take integer as input and check if it is even or odd.
numm =int(input("Enter number :"))
if numm % 2==0:
    print("The number is even")
elif numm%3==0:
    print("The number is odd")
else:
    print("not even or odd")
