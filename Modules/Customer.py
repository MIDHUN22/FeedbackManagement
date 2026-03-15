from tabulate import tabulate
from Models.feedback_model import FeedbackModel
from Models.user_model import UserModel
from Models.product_model import ProdctModel
from Models.customer_model import CustomerModel
from Models.db import Database
class Customer:

    def __init__(self,customer_id):
        self.customer_id = customer_id
        self.feedback_model=FeedbackModel()
        self.user_model=UserModel()
        self.product_model=ProdctModel()
        self.customer_model=CustomerModel()

    def menu(self):
        while True:
            print("\n--- Customer Menu ---\t1. View Products\t2. View Feedbacks\t3. Add Feedback\t4.Logout ")

            choice = input("Enter choice: ")

            if choice == "1":
                print("Viewing Products...")
                self.ViewAllProducts()

            elif choice == "2":
                print("Listing Feedbacks---")
                self.ViewAllFeedback()
               
            elif choice == "3":
                print("Let's Add Some Feedbacks...")
                self.AddFeedBack()
            elif choice == "4":
                print("Logging out...")
                break

            else:
                print("Invalid choice")
                
    
    def ViewAllFeedback(self):
        print("Customer ID:", self.customer_id)

        feedbacks = self.feedback_model.get_all_customer_feedback(self.customer_id)

        if not feedbacks:
            print("No Feedbacks Found")
            return

        headers = ["Username", "Product", "Comment", "Rating", "Status"]

        print(tabulate(feedbacks, headers=headers, tablefmt="grid"))

            
    def AddFeedBack(self):
        print('_________Creating Feedback__________')
        
        self.ViewAllProducts()

        product_id=int(input("Enter The Product ID:\t"))
        comment=input("Enter Your Comment:\t")
        rating=int(input("Enter Your Rting (1 to 5):\t"))

        if rating < 1 or rating > 5:
            print("Rating must be between 1 and 5")
            return
        self.feedback_model.create_feedback(self.customer_id,product_id,rating,comment)
        print("Feedback Added!!!")

    def ViewAllProducts(self):
        print('_________Available Products__________')
        products=self.product_model.ViewAllProducts()
        if not products:
            print("No Products Available At The Time!!!!")
            return
        headers=["Product ID", "Product Name", "Category"]
        print(tabulate(products, headers=headers, tablefmt="grid"))