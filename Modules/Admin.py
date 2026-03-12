class Admin:

    def menu(self):
        while True:
            print("\n--- Admin Menu ---\n1. View Feedback\t2. Manage Products\n3. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                print("Viewing feedback...")

            elif choice == "2":
                print("Managing products...")

            elif choice == "3":
                print("Logging out...")
                break

            else:
                print("Invalid choice")