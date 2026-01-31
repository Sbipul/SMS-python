from student import Student
from validation import Validation

class Helper:
    @staticmethod
    def check_duplicate_roll(roll, students):
        for st in students:
            if st.get("roll") == roll:
                return True
        return False
    
    @staticmethod
    def show_students(students):
        for st in students:
            print(f"{'ID':<12} : {st["id"]}")
            print(f"{'Name':<12} : {st["name"]}")
            print(f"{'Roll':<12} : {st["roll"]}")
            print(f"{'Email':<12} : {st["email"]}")
            print(f"{'Department':<12} : {st["department"]}\n\n")
            
    @staticmethod
    def get_student_info():
        name = Validation.get_valid_name()
        roll = Validation.get_valid_roll()
        email = Validation.get_valid_email()
        department = Validation.get_valid_department()
        return Student(name, roll, email, department)