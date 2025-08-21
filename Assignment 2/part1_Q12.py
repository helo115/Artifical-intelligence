#12.Write a program that takes a temperature in Celsius and checks if it is freezing, moderate or hot.
#a.	Freezing temperature is below 0.
#b.	Moderate temperature is greater than 0 and less than 26.
#c.	Hot temperature is above 26.
celsius=int(input("Enter the temperature :"))
#a.	Freezing temperature is below 0.
if celsius<0:
    print("It is freezing :")
#b.	Moderate temperature is greater than 0 and less than 26.    
elif celsius>=0 and celsius <26:
    print("It is moderate")
#c.	Hot temperature is above 26.    
else:
    print("It is hot")

