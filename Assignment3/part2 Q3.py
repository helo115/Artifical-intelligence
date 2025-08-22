#3.	Create a list [“apple”, “raspberry”, “pineapple”, “cherry”]. 
#a.	 How can you check if apple is present in the list and get the index of the element (if present)
#b.	Now replace the raspberry and pineapple with orange.
#c.	Insert “apricot” at index 2.
#d.	Extend the resulting list with items “car”, “bike”, “aeroplane”.

#a.	 How can you check if apple is present in the list and get the index of the element (if present)
list = ["apple", "raspberry", "pineapple", "cherry"]

if "apple" in list:
    result=list.index("apple")
    print(result)
else:
    print("apple is not in the list")

#b.	Now replace the raspberry and pineapple with orange.
list[1:3]=["ornge"]
print(list)

#c.	Insert “apricot” at index 2.
list.insert(2,"apricot")
print( list)

#d.	Extend the resulting list with items “car”, “bike”, “aeroplane”.
list.extend(["car","bike","aeroplane"])
print(list)
