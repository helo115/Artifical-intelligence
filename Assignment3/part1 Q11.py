#11.	Write a function to compute factorial of a given number using recursion technique.
n=int(input("enter a number"))
def factorial(n):
    if n>0:
        result=n*factorial(n-1)
    else:
        result=1
    return result

hi=factorial(n)
print(hi)
