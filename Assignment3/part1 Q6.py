#6.Write a function to take integer as argument and check if it is even or odd.
integer=int(input("Enter the number"))
def func(integer):
    if integer%2==0:
        return "it is even number"
    else:
        return "it is odd number"
hi=func(integer)
print(hi)
