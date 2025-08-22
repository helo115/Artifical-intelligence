#6.	From the given list:
#Gadgets = [“Mobile”, “Laptop”, 10.0, “Marker”, 3, 10, “Speakers”, “Camera”, 310.25]
#a.	Create separate list of string and numbers,
#b.	Sort the string list in ascending and descending order
#c.	Sort the string list by length of elements in the list
#d.	Sort the numbers list in ascending and descending order

#a.	Create separate list of string and numbers,
a = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]
b=[]
c=[]
for i in a:
    if  isinstance(i,str):
        b.append(i)
        
        
for x in a:
    if isinstance(x,(int,float)):
        c.append(x)


print(b)
print(c)
#b.	Sort the string list in ascending and descending order

b.sort()
print(b)
b.sort(reverse=True)
print(b)

#c.	Sort the string list by length of elements in the list
b.sort(key=len)
print(b)


#d.	Sort the numbers list in ascending and descending order
c.sort()
print(c)
c.sort(reverse=True)
print(c)
