#5.	Create a list [32,54,66,11,77,10,90]
#a.	Remove items from the list with values less than 20.
#b.	Sort the list in ascending and descending order.
#c.	Now, compute the average value of the list items.


#a.	Remove items from the list with values less than 20.
list=[32,54,66,11,77,10,90]
for i in list:
    if i > 20:
        print(i)


        
#b.	Sort the list in ascending and descending order.

list.sort()
print(list)
list.sort(reverse=True)
print(list)        
    
    
#c.	Now, compute the average value of the list items.
list=[32,54,66,11,77,10,90]
b=0
for a in list:
    b+=a

    
average=b/7
print(average)
