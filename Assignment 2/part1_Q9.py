#9.	Write a program that ask for an integer number and checks if it is divisible by 2, 3, or both.
number=int(input("Enter Integer number"))
if number % 2==0 and number % 3==0:
    print("This is divisible by both 2 and 3")
elif number%2==0:
    print("this is divisible by 2 ")
elif number%3==0:
    print("This is divisible by 3 ")
else:
    print("not divisible by both ")
