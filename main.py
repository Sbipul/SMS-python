from student import Student
from database import Database
from request import Request

print("Welcome to the Student Record Management System!")
Database.connect_database()


while True:
    print("==================== MENU ====================")
    print("01.Add Student")
    print("02.View Student")
    print("03.Search Student")
    print("04.Remove Student")
    print("05.Exit")
    print("==============================================")

    item = int(input("Enter your choice : "))
    if item == 5:
        break

    elif item==1:
        student = Database.get_student_info()
        Request.add_student(student)

    elif item==2:
        all_students = Request.get_student()
        Database.show_students(all_students)
        
    elif item==3:
        search_text = input("Enter email/roll/name to search student : ")
        searched_students = Request.search_student(search_text)
        Database.show_students(searched_students)

    elif item==4:
        roll = input("Enter student roll no : ")
        confirmation = input(f"Are you sure want to remove this roll {roll}? (y/n)")
        if confirmation.lower() in ['y', 'yes']:
            Request.delete_student(roll)
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")    