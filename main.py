from Modules.Authentication import Authentication
from Modules.Admin import Admin
from Modules.Customer import Customer
from Models.customer_model import CustomerModel


class MainApp:

    def __init__(self):
        self.auth = Authentication()

    def run(self):
        while True:
            try:
                print("\nWelcome to Feedback System")
                print("1. Login")
                print("2. Register")
                print("3. Exit")

                choice = input("Enter choice: ").strip()

                if choice == "1":
                    self.handle_login()

                elif choice == "2":
                    self.handle_register()

                elif choice == "3":
                    print("Exiting...")
                    break

                else:
                    print("Invalid choice! Please select 1–3.")

                input("\nPress Enter to continue...")

            except Exception as e:
                print("Unexpected error occurred:", e)

    # ---------------- LOGIN ----------------
    def handle_login(self):
        try:
            result = self.auth.Login()

            if not result:
                return

            user_id, role = result

            if role == "Admin":
                Admin().menu()

            elif role == "Customer":
                customer_model = CustomerModel()
                customer_data = customer_model.get_customer_by_user_id(user_id)

                if customer_data:
                    customer_id = customer_data[0]
                    Customer(customer_id).menu()
                else:
                    print("Customer Not Found")

            else:
                print("Invalid role returned")

        except Exception as e:
            print("Error during login:", e)

    # ---------------- REGISTER ----------------
    def handle_register(self):
        try:
            print("\nRegister as:\t1.Admin\t2.Customer")

            role_choice = input("Enter choice: ").strip()

            if role_choice == "1":
                self.auth.register("Admin")

            elif role_choice == "2":
                self.auth.register("Customer")

            else:
                print("Invalid role choice")

        except Exception as e:
            print("Error during registration:", e)


# ---------------- ENTRY POINT ----------------
if __name__ == "__main__":
    app = MainApp()
    app.run()