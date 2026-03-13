from Modules.Authentication import Authentication
from Modules.Admin import Admin
from Modules.Customer import Customer
from Modules.Feedback import Feedback


class MainApp:

    def run(self):

        try:
            print("Welcome to Feedback System")

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

                else:
                    print("Invalid role returned")

            elif choice == "2":

                print("\nRegister as: \t1.Admin\t2.Customer")

                role_choice = input("Enter choice: ")

                if role_choice == "1":
                    auth.register("Admin")

                elif role_choice == "2":
                    auth.register("Customer")

                else:
                    print("Invalid role choice")

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid input! Please enter correct value")

        except Exception as e:
            print("Something went wrong:", e)


if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()