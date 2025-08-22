#List = [“Tahir”, 44, “AI and Data Science”, True]
#2.Write a code to separate strings, numbers and Boolean data from the above list into separate lists.
list1=["Tahir", 44, "AI and Data Science", True]
list2=[]
list3=[]
list4=[]
for item in list1:
     if isinstance (item,str):
         list2.append(item)

     elif isinstance (item,bool):
        list3.append(item)


     elif  isinstance (item,int):
         list4.append(item)


print(list2)
print(list3)
print(list4)
