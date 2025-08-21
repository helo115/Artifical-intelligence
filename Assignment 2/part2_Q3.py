#3.	Write a program to print multiplication table of a given number.

num=int(input("Enter number :"))

for i in range(1,11,1):
    print(f"{num}x{i}=",num*i)
