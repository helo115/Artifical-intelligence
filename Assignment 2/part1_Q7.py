#7. Write a program to take two numbers and an operator (/,x,+,-) as input and perform the corresponding operation.

num1=int(input("Enter number 1 :"))
num2=int(input("Enter number 2 :"))
operator=input("Enter operator (+,-,*,/) :")
if operator=="+":
    num=num1+num2
    print("Addition of two number is :",num)
elif operator=="-":
    num=num1-num2
    print("Subtraction of two number is :",num)
elif operator=="*":
    num=num1*num2
    print("Multiplication of two number is :",num)
elif operator=="/":
    if num2==0:
        print("Zero is not divisible :")
    else:
        num=num1/num2
        print("division of two number is :",num)
else:
    print("Invalid operator")
