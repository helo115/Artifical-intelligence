##5.	Write a program to take user’s age as input and display whether he is minor, adult or senior citizen:
#a.	Minor age is less than 18.
#b.	Adult age is greater than 18 and less than 60
#c.	Senior citizen age is greater than 60        
userage=int(input("Enter Age :"))
#a. Minor age is less than 18.
if userage<18:
    print("he is minor")
#b.Adult age is greater than 18 and less than 60
elif userage>=18 and userage<60:
    print("he is adult")
#c.Senior citizen age is greater than 60
else:
    print("he is senior citizen")
    
