#2.Write a function that takes a number as argument and check if a given number is positive, negative or zero.
num=int(input("Enter the number"))
def check(num):
    if num>0:
        print("This number is positive")
    elif num<0:
        print("This number is negative")
    else:
        print("The number is zero")


check(num)
