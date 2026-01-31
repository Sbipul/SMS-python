class Validation:
    @staticmethod
    def get_valid_name():
        while True:
            name = input("Enter Student Name : ").strip()
            if len(name) < 3:
                print("❌ Name must be at least 3 characters")
            elif not name.replace(" ", "").isalpha():
                print("❌ Name must contain only letters")
            else:
                return name

    @staticmethod
    def get_valid_roll():
        while True:
            roll = input("Enter Student Roll : ").strip()
            if not roll.isdigit():
                print("❌ Roll must contain numbers only")
            elif len(roll) < 2:
                print("❌ Roll must be at least 2 digits")
            else:
                return int(roll)   # optional: return as number instead of string


    @staticmethod
    def get_valid_email():
        while True:
            email = input("Enter Student Email : ").strip()

            if "@" not in email or "." not in email:
                print("❌ Invalid email format")
            else:
                return email

    @staticmethod
    def get_valid_department():
        while True:
            dept = input("Enter Student Department : ").strip()
            if len(dept) < 3:
                print("❌ Department must be at least 3 characters")
            elif not dept.replace(" ", "").isalpha():
                print("❌ Department must contain only letters")
            else:
                return dept