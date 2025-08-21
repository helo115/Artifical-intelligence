#Bonus Challenge:
#Write a program to print the first 10 Fibonacci numbers using for loop.
#Hint: First 10 Fibanacci numbers are  0,1,1,2,3,5,8,13,21,34Bonus Challenge:


a, b = 0, 1 
print(a)   
print(b)     

for i in range(8):
    c = a + b
    print(c)        
    a, b = b, c
