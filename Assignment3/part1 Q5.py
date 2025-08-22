#5. Write a function to take user’s age as argument and return the message from the function whether he is minor, adult or senior citizen:
#a. Minor age is less than 18.
#b. Adult age is greater than 18 and less than 60
#c. Senior citizen age is greater than 60

age=int(input("Enter the age :"))
def program(age):
     if age<18:
         return "he is minor citizen"
     elif age>=18 and age<60:
         return "he is adult citizen"
     else:
        return"he is senior citizen "

result=program(age)
print(result)
