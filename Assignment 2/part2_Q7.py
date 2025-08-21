#7.	Write a program to compute the factorial of a number using while loop.
n=int(input("Enter number "))

if n<0:
    print("unable to  find factorial negative number ")
else:
    factorial=1
    i=1
    while n>=i:
        factorial=factorial*i
        i=i+1
    print("factorial of",n,"is",factorial)

