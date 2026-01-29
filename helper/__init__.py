from student import Student


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
        name = input("Enter Student Name : ")
        roll = input("Enter Student Roll : ")
        email = input("Enter Student Email : ")
        department = input("Enter Student Department : ")
        return Student(name, roll, email, department)