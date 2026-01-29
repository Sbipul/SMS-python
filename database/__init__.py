import time
class Database:

    @staticmethod
    def connect_database():
        for i in range(101):
            print(f"\rLoading students {i}% ", end="")
            time.sleep(0.02)

        print("\nDatabase connected ✅\n\n\n")

    


