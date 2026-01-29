import time
class Database:

    @staticmethod
    def connect_database():
        for i in range(101):
            # print(f"\rLoading students {i}% ", end="")
            # time.sleep(0.01)
            print(f"\r\033[34mLoading students {i}%\033[0m", end="")
            time.sleep(0.02)

        print("\n\033[32m***** Database connected *****\033[0m\n\n\n")

    


