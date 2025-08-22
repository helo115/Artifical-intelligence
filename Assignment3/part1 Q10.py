#10.	Write a function that evaluates if an input number is prime.
def func():
    while True:
        number=int(input("enter a number"))
        num=number+1
        if num % 2==0 or num==3:
            return"program is evaluates"
            break
        else:
            print("enter again")
hi=func()
print(hi)
