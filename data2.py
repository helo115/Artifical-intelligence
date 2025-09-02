# Hands-on exercise on List and its built-in methods (append, index, remove, sort)

# Task: Write a menu-driven program to create a Student Records Management System using
#               List and Dic methods
#  1. Add Student - Take name, roll number, subject and marks as input and store them in a list
#  2. Display students - show all stored students in a readable format
#  3. Search Student - Search for a student by roll number and display if found
#  4. update record - Update the marks of student using roll number
#  5. Delete Record - Delete a student record using roll number
#  6. Sort Record - Sorting students records by marks or name
#  7. Exit

# initalize list for store student record.
dics=[]
# add function
def add_dic():
    n=input("Enter the name")
    r=input("Enter the roll no")
    c=input("Enter the course ")
    m=int(input("Enter the Marks "))
    dics.append({"name":n,"roll_no":r,"course":c,"marks":m})

# Display function
def Display_dics():
    
    if dics:
        for i in dics:
            print(f"name:{i['name']}")
            print(f"Rollno:{i['roll_no']}")
            print(f"course:{i['course']}")
            print(f"Marks:{i['marks']}")
            
    else:
        print("list is Empty ")
# Search Function
def Search_dics():
    if dics:
        roll_no=input("Enter the roll no :")
        for index,found in enumerate( dics):
           if roll_no==found['roll_no']:
               return found,index
                
        return None,None 
    else:
         print("List is empty")
         return None,None
# update function
def  update_dics():
    dics_found, index = search_dics()
    if dics is not None:
        #get marks and update    
        print("---------------")
        print("Record Found")
        print("---------------")
        print(f"Name: {dics_found[0]}")
        print(f"Roll No: {dics_found[1]}")
        print(f"Course: {dics_found[2]}")
        print(f"Marks: {dics_found[3]}")
        print("---------------")
        # get new marks to update
        update_marks = int(input("Enter marks to update:"))
        # update marks in records
        students_records[index][3] = update_marks
        print("Record Successfully updated...")
    else:
        print("Record not Found! \nUnable to update")
# 5 delete function 
def  delete_dics():
     dics_found, _ = search_dics()
     if dics_found is not None:
         # delete record i.e. remove found student record from the records
         dics_records.remove(student_found)
         print("Deleted Record successfully")
     else:
         print("Record not found! \nUnable to delete")
# 6.sort function
def dics_sort():
          if dics:
             # sort by marks [marks are saved at 3rd index of nested dics  list]
             dics.sort(key=lambda x:x[3], reverse=True)     # x = [name1, roll_no1, course1, marks1]  then x[3] will be marks1
             print("Records sorted by Marks successfully....") 
          else:
             print("Empty Records!!! \nUnable to Sort")
    
# for repeat user the menu we need loop so we done while loop because we didnot need to tell to run how many time.
while True:
    print("1. Add Student ")
    print("2. Display students ")
    print("3. Search Student")
    print("4. update record")
    print("5. Delete Record")
    print("6. sort Record")
    print("7. Exit")

 #declare variable which ask user to enter the choice.
    choose=input("Enter Your Choose")
    #Add student.
    if choose=='1':
        add_dic()
    if choose=='2':
        Display_dics()
    if choose=='3':
        record,_=Search_dics()
        if record is not None:
            print(f"name:{record['name']}")
            print(f"Rollno:{record['roll_no']}")
            print(f"course:{record['course']}")
            print(f"Marks:{record['marks']}")
        else:
            print("Record not found")

    if choose=='4':
        record,index=Search_dics()
        if record is not None:
            marks=int(input("Enter the marks:"))
            dics[index]['marks']=marks
            print("Successfully updated")
        else:
            print("Record not found")
    if choose=='5':
        record,index=Search_dics()
        if record is not None:
            dics.remove(record)
            print("Successfully Deleted")
        else:
            print("Record not found")
    if choose=='6':
        if dics:
            st=input("Type 'Asscending'or'Descending':")
            if st=="Asscending":
                dics.sort(key=lambda x:x['marks'],)
                print("Successfully sorted")
            if st=='Descending':
                dics.sort(key=lambda x:x['marks'],reverse=True)
                print("Successfully updated")
        else:
            print("Record is empty")

    if choose=='7':
        break
