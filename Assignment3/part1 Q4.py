#4.Write a function to take three numbers as argument and return the largest number
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
def func(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("The larger number is")
        return num1
    elif num2>num1 and num2>num3:
        print("The larger number is")
        return num2
    elif num3>num1 and num3>num2:
        print("The larger number is ")
        return num3
    else:
        return "All are sama"
    


hi=func(num1,num2,num3)
print(hi)
