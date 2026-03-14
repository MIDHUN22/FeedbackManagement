class Admin:

    def __init__(self):
        self.feedback_model=FeedbackModel()
        self.user_model=UserModel()
        self.product_model=ProdctModel()

    def menu(self):
        while True:
            print("\n--- Admin Menu ---\n1. View Feedback\t2. Manage Products\n3. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                print("Viewing feedback...")
                self.ViewAll()

            elif choice == "2":
                print("Managing products...\t1.Add Product\t2.View All Product")
                prod_choice=int(input("Enter Your Choice:"))

                if prod_choice=="1":
                    print("Adding Product")
                    self.CreateProdct()
                elif prod_choice=="2":
                    print("Viewing Procts")
                    self.ViewAllProducts()
                else:
                    print("Invald Input")

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
            


