from database import Database
from request import Request
from helper import Helper

print("\n\nWelcome to the Student Record Management System!")
Database.connect_database()


while True:
    print("==================== MENU ====================")
    print("1.Add Student")
    print("2.View Student")
    print("3.Search Student")
    print("4.Remove Student")
    print("5.Exit")
    print("==============================================")

    item = int(input("Enter your choice : "))
    if item == 5:
        break

    elif item==1:
        student = Helper.get_student_info()
        Request.add_student(student)

    elif item==2:
        all_students = Request.get_student()
        Helper.show_students(all_students)
        
    elif item==3:
        search_text = input("Enter email/roll/name to search student : ")
        searched_students = Request.search_student(search_text)
        Helper.show_students(searched_students)

    elif item==4:
        roll = input("Enter student roll no : ")
        confirmation = input(f"Are you sure want to remove this roll {roll}? (y/n) : ")
        if confirmation.lower() in ['y', 'yes']:
            Request.delete_student(roll)
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")    