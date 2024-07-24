import sys
from dbhelper import DBhelper

class Flipkart:

    def __init__(self):
        # connect to database
        self.db = DBhelper()

        self.menu()

    def menu(self):
        while True:
            user_input = input('''
            1. Enter 1 to Register
            2. Enter 2 to login
            3. Enter anything else to leave''')


            if user_input == "1":
                self.register()
            elif user_input == "2":
                self.login()
            else:
                sys.exit(1000)

    def login_menu(self):
        input("""
              1. Enter 1 to see profile
              2. Enter 2 to edit profile
              3. Enter 3 to delete profile
              4. Enter 4 to logout 
              """)


    def register(self):
        name = input("Enter the Name")
        email = input("Enter your email")
        password = input("Enter your password")


        response = self.db.register(name,email, password)

        if response:
            print("Registration successful")
        else: 
            print("Registration failed")


    def login(self):
        email = input("Enter your email")
        password = input("Enter your password")

        data = self.db.search(email, password)

        if len(data) == 0:
            print("Access denied")
            self.login()

        else:
            print("Hello", data[0][1])
            
        self.login_menu()


        





if __name__ == "__main__":
    Flipkart()
