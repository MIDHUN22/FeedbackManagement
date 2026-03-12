class Admin:

    def __init__(self):
        self.feedback_model=FeedbackModel()
        self.user_model=UserModel()

    def menu(self):
        while True:
            print("\n--- Admin Menu ---\n1. View Feedback\t2. Manage Products\n3. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                print("Viewing feedback...")
                self.ViewAll()

            elif choice == "2":
                print("Managing products...")

            elif choice == "3":
                print("Logging out...")
                break

            else:
                print("Invalid choice")
                return
    
    def ViewAll(self):
        feedbacks=self.feedback_model.get_all_feedback()

        if not feedbacks:
            print('No FeedBacks Found')
            return
        print('Feedbacks Are..')
        for fb in feedbacks:
            print(fb)
            


