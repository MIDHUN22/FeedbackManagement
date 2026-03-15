from tabulate import tabulate
from Models.feedback_model import FeedbackModel
from Models.user_model import UserModel
from Models.product_model import ProdctModel
from Models.db import Database

class Admin:

    def __init__(self):
        self.feedback_model=FeedbackModel()
        self.user_model=UserModel()
        self.product_model=ProdctModel()

    def menu(self):
        while True:
            print("\n--- Admin Menu ---\n1. Manage Feedback\t2. Manage Products")

            choice = input("Enter choice: ")

            if choice == "1":
                # self.ViewAll()
                print("Manageing Feedbacks...\t1.View All Feedbacks\t2.Change Status\t3 LogOut ")
                feed_choice=int(input('Enter Your Choice:'))

                if feed_choice==1:
                    print("Viewing Feedbacks")
                    self.ViewAllFeedback()
                elif feed_choice==2:
                    print("Change Status")
                    self.ChangeStaus()
                else:
                    print("Invald Input")

            elif choice == "2":
                print("Managing products...\t1.Add Product\t2.View All Product")
                prod_choice=int(input("Enter Your Choice:"))

                if prod_choice==1:
                    print("Adding Product")
                    self.CreateProdct()
                elif prod_choice==2:
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
    
    def ViewAllFeedback(self):
        feedbacks=self.feedback_model.get_all_feedback()

        if not feedbacks:
            print('No FeedBacks Found')
            return
        print('Feedbacks Are..')
        # for fb in feedbacks:
        #     print(fb)
        headers = ["Feedback ID", "Customer ID", "Product ID", "Rating", "Comment", "Status", "Created At"]
        print(tabulate(feedbacks, headers=headers, tablefmt="grid"))

    def ChangeStatus(self):

        feedback_id = int(input("Enter Feedback ID: "))

        print("1. Approve Feedback\t2. Reject Feedback")

        choice = input("Enter choice: ")

        if choice == "1":
            status = "Approved"

        elif choice == "2":
            status = "Rejected"

        else:
            print("Invalid choice")
            return

        self.feedback_model.change_status(feedback_id, status)

        print("Feedback status updated successfully")


    def ViewAllProducts(self):
        products = self.product_model.ViewAllProducts()

        if not products:
            print("No products Found")
            return

        headers = ["Product ID", "Product Name", "Category"]

        print(tabulate(products, headers=headers, tablefmt="grid"))

    def CreateProdct(self):
        print("Enter The Product Details...")
        product_name=input("Enter Product Name:\t")
        product_cat=input("Enter Product Category:\t")

        self.product_model.CreateProdct(product_name,product_cat)
        print('Product Created!')
