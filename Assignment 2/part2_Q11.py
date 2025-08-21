#11.	Write a program to calculate the sum of even and odd numbers and print them. (numbers from 1 to 50)
total=0
for i in range(0,51,2):
        total+=i
        
num=0
for n in range(1,50,2):
    num+=n

print("the sum of even and odd number is ",num+total)
