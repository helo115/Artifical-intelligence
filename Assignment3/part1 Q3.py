#3.Write a function to take two numbers as arguments and return the larger number.
num1=int(input("Enter number 1 :"))
num2=int(input("Enter number 2 :"))
def function(num1,num2):
    if num1>num2:
        print("The number 1 is greather ")
        return num1
    elif num2>num1:
        print("The number 2 is greather ")
        return num2
    else:
        return "Both are equal"

result=function(num1,num2)
print(result)
