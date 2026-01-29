from helper import Helper

class Request:

    @staticmethod
    def get_student(filepath="data/data.txt"):
        all_students = []

        try:
            with open(filepath, 'r') as f:
                for line in f:
                    data = line.strip().split(",")

                    if len(data) != 5:
                        continue

                    student_dict = {
                        "id": data[0],
                        "name": data[1],
                        "roll": data[2],
                        "email": data[3],
                        "department": data[4]
                    }

                    all_students.append(student_dict)

        except FileNotFoundError:
            print("File not found!")

        return all_students

    @staticmethod
    def add_student(student):
        all_students = Request.get_student()
        check_existing = Helper.check_duplicate_roll(student.roll,all_students)

        if check_existing:
            print(f"{student.roll} is already exist.")
            return

        if all_students:
            last_id = all_students[-1]["id"]
            id = int(last_id)+1
        else:
            id = 1

        try:
            line = f"\n{id},{student.name},{student.roll},{student.email},{student.department}"
            with open("data/data.txt",'a') as f:
                f.write(line)
            print("Student added successfully")

        except FileNotFoundError:
            print("File not found")
    
    @staticmethod
    def delete_student(roll):
        all_students = Request.get_student()
        remain = [student for student in all_students if student['roll'] != roll]
        if remain:
            try:
                with open("data/data.txt", "w") as f:
                    for student in remain:
                        line = f"{student['id']},{student['name']},{student['roll']},{student['email']},{student['department']}\n"
                        f.write(line)
                print(f"{roll} has been deleted. Remaining students")
            except FileNotFoundError:
                print("File not found")
        else:
            print("No student found")

    
    @staticmethod
    def search_student(searchtext):
        all_student = Request.get_student()
        result = [s for s in all_student if searchtext.lower() in s['roll'].lower() or searchtext.lower() in s['email'].lower() or searchtext.lower() in s['name'].lower()]
        return result