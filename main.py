from Modules.Authentication import Authentication
from Modules.Admin import Admin
from Modules.Customer import Customer
from Modules.Feedback import Feedback


class MainApp:

    def run(self):

        print("Welcome to Customer Feedback System")

        auth = Authentication()

        print("1. Login")
        print("2. Register")

        choice = input("Enter choice: ")

        if choice == "1":
            role = auth.Login()

            if role == "Admin":
                admin = Admin()
                admin.menu()

            elif role == "Customer":
                customer = Customer()
                customer.menu()

        elif choice == "2":
            auth.register()

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()