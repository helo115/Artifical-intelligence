#  1. Add Student - Take name, roll number, subject and marks as input and store them into a list
#  2. Display students - show all stored students records in a readable format
#  3. Search Student - Search for a student by roll number and display if found
#  4. update recored - Update the marks of student using roll number
#  5. Delete Record - Delete a student record using roll number
#  6. Sort Record - Sorting students records by marks
#  7. Exit

# for storing students records
# Each student should have [name, roll_no, course, marks]
list_records = []

# 1. Add records
def add_records():
    name = input("Enter student name:")
    roll_no = input("Enter student roll no:")
    course = input("Enter student course: ")
    marks = int(input("Enter student marks:"))
    students_records.append([name, roll_no, course, marks])
    print("Student added successfully...")

# 2. display records
def display_records():
    if list_records:
        print("------------------")
        print("list records")
        print("------------------")
        for list in list_records:
            print(f"Name: {list[0]}")
            print(f"Roll no: {list[1]}")
            print(f"Course: {list[2]}")
            print(f"Marks: {list[3]}")
            print("-----------------------")
    else:
        print("No record found. Enter records first")

# 3. Search list from records
def search_records():
    # check if list record is not empty
    if list_records:
        roll_no = input("Enter roll no of list:")

        # Method1 ----------------------------------------------
        for index, list in enumerate(list_records):
            if roll_no == list[1]:  # roll no is at index 1
                #found = True
                return list, index    # list_records.index(student)
          # If not found then print the error message
        return None, None

    else:
        print("Unable to search. Please enter records first....")
        return None, None

# 4. Update the marks using roll no
def update_marks():
    list_found, index = search_records()
    if list_found is not None:
        # get marks and update records
        print("---------------")
        print("Record Found")
        print("---------------")
        print(f"Name: {list_found[0]}")
        print(f"Roll No: {list_found[1]}")
        print(f"Course: {list_found[2]}")
        print(f"Marks: {list_found[3]}")
        print("---------------")
        # get new marks to update
        update_marks = int(input("Enter marks to update:"))
        # update marks in records
        list_records[index][3] = update_marks
        print("Record Successfully updated...")
    else:
        print("Record not Found! \nUnable to update")
    
# 5. Delete records by marks
def delete_record():
    list_found, _ = search_records()
    if list_found is not None:
        # delete record i.e. remove found student record from the records list
        list_records.remove(list_found)
        print("Deleted Record successfully")
    else:
        print("Record not found! \nUnable to delete")
    

# 6. Sort records by marks
def sort_records():
    if list_records:
        # sort by marks [marks are saved at 3rd index of nested student record list]
        list_records.sort(key=lambda x:x[3], reverse=True)     # x = [name1, roll_no1, course1, marks1]  then x[3] will be marks1
        print("Records sorted by Marks successfully....")
        
    else:
        print("Empty Records!!! \nUnable to Sort")
    
while True:
    print("-----------------------------")
    print("1. Add  Records.")
    print("2. Display  Records.")
    print("3. Search  Record.")
    print("4. Update  Record.")
    print("5. Delete  Record.")
    print("6. Sort Records")
    print("7. Exit")
    print("-----------------------------")

    option = input("Enter your option:")

    if option == '1':
        # Add record
        add_records()
    elif option == '2':
        # Display Records
        display_records()
    elif option == '3':
        # Search record
        list_, _ = search_records()
        if list_ is not None:
            print("---list found---")
            print(f"Name: {list_[0]}")
            print(f"Roll no: {list_[1]}")
            print(f"Course: {list_[2]}")
            print(f"Marks: {list_[3]}")
        else:
            print("Record not found !!!")
    elif option == '4':
        # Update list record
        update_marks()
    elif option == '5':
        # Delete list record
        delete_record()
    elif option == '6':
        # sort records
        sort_records()
    elif option == '7':
        # Exit
        break
    else:
        print("Invalid Choice!!!")
