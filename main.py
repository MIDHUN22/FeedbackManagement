from Modules.Authentication import Authentication
from Modules.Admin import Admin
from Modules.Customer import Customer
from Modules.Feedback import Feedback
from Models.customer_model import CustomerModel



class MainApp:

    def run(self):

        try:
            print("Welcome to Feedback System")

            auth = Authentication()

            print("1. Login")
            print("2. Register")

            choice = int(input("Enter choice: "))

            if choice == 1:

                result = auth.Login()
                if result:
                    user_id, role = result

                    if role == "Admin":
                        admin = Admin()
                        admin.menu()

                    elif role == "Customer":
                        customer_model = CustomerModel()
                        result = customer_model.get_customer_by_user_id(user_id)
                        if result:
                            customer_id = result[0]
                            customer = Customer(customer_id)
                            customer.menu()
                        else:
                            print("Customer Not Found")

                    else:
                        print("Invalid role returned")

            elif choice == 2:

                print("\nRegister as: \t1.Admin\t2.Customer")

                role_choice = input("Enter choice: ")

                if role_choice == "1":
                    auth.register("Admin")

                elif role_choice == "2":
                    auth.register("Customer")

                else:
                    print("Invalid role choice")

            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input! Please enter correct value")

        except Exception as e:
            print("Something went wrong:", e)


while True:
    main_app = MainApp()
    main_app.run()