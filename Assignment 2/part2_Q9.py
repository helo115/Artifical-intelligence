#9.	Write a program that continues to ask user to input password until the correct password is entered.

while True:
    password=input("Enter Password")
    if password=="hello123":
        print("password is corrected")
        break
    else:
        print("Password is wrong try again")
        
