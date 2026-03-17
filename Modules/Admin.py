from tabulate import tabulate
from Models.feedback_model import FeedbackModel
from Models.user_model import UserModel
from Models.product_model import ProdctModel
from Models.customer_model import CustomerModel

class Admin:

    def __init__(self):
        self.feedback_model=FeedbackModel()
        self.user_model=UserModel()
        self.product_model=ProdctModel()
        self.customer_model = CustomerModel()

    def menu(self):
        while True:
            try:
                print("\n--- Admin Menu ---\n1. Manage Feedback\t2. Manage Products\t3 .Manage Customers\t4. Logout ")

                choice = input("Enter choice: ")

                if choice == "1":
                    try:
                        self.ManageFeedback()
                    except Exception as e:
                        print("Error in Feedback Management:", e)

                elif choice == "2":
                    try:
                        self.ManageProducts()
                    except Exception as e:
                        print("Error in Product Management:", e)

                elif choice == "3":
                    try:
                        self.ManageCustomer()
                    except Exception as e:
                        print("Error in Customer Management:", e)

                elif choice == "4":
                    print("Logging out...")
                    break

                else:
                    print("Invalid choice! Please select 1–4.")

                input("\nPress Enter to continue...")

            except Exception as e:
                print("Unexpected error occurred:", e)

    def ManageFeedback(self):
        print("Managing Feedbacks...\n1.View All Feedbacks\t2.Change Status\t3. Delete Feedback\t4 Admin Menu ")

        try:
            feed_choice = int(input('Enter Your Choice: '))
        except ValueError:
            print("Invalid input! Enter a number.")
            return

        if feed_choice == 1:
            self.ViewAllFeedback()
        elif feed_choice == 2:
            self.ChangeStatus()
        elif feed_choice == 3:
            self.DeleteFeedback()
        elif feed_choice == 4:
            return
        else:
            print("Invalid Input")

    def ViewAllFeedback(self):
        feedbacks=self.feedback_model.get_all_feedback()

        if not feedbacks:
            print('No FeedBacks Found')
            return
        print('Feedbacks Are..')
    
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
    
    def DeleteFeedback(self):
        self.ViewAllFeedback()

        try:
            feedback_id = int(input("Enter Feedback Id To Be Deleted:\t"))
        except ValueError:
            print("Invalid input! Enter a valid number.")
            return

        confirm = input("Are you sure? (y/n): ")

        if confirm.lower() == "y":
            try:
                self.feedback_model.delete_feedback(feedback_id)
                print("Feedback Deleted!")
            except Exception as e:
                print("Error deleting feedback:", e)
        else:
            print("Cancelled")

    def ManageProducts(self):
        print("Managing products...\n1. Add Product\t2. View All Product\t3. Delete Product\t4. Admin Menu")

        try:
            prod_choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            return

        if prod_choice == 1:
            self.CreateProdct()
        elif prod_choice == 2:
            self.ViewAllProducts()
        elif prod_choice == 3:
            self.DeleteProduct()
        elif prod_choice == 4:
            return
        else:
            print("Invalid Input")


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

    def DeleteProduct(self):
        self.ViewAllProducts()

        try:
            product_id = int(input("Enter the product Id You Want To Delete:\t"))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return

        confirm = input("Are you sure? (y/n): ")

        if confirm.lower() == "y":
            try:
                self.product_model.DeleteProduct(product_id)
                print("Product Deleted Successfully")
            except Exception as e:
                print("Error deleting product:", e)
        else:
            print("Cancelled")    

    def ManageCustomer(self):
        try:
            self.ViewAllCustomers()

            print("CUSTOMER MANAGEMENT\n1. View All Customers \t2. Block Customer\t3. Delete Customer\t4. Admin Menu")
            cust_choice = input("Enter Your Choice\t: ").strip()

            if cust_choice == "1":
                self.ViewAllCustomers()

            elif cust_choice == "2":
                try:
                    self.BlockCustomer()
                except Exception as e:
                    print("Error while blocking customer:", e)

            elif cust_choice == "3":
                try:
                    self.DeleteCustomer()
                except Exception as e:
                    print("Error while deleting customer:", e)

            elif cust_choice == "4":
                return

            else:
                print("Invalid option! Please choose between 1-4.")

        except Exception as e:
            print("Something went wrong in Customer Management:", e)

    def ViewAllCustomers(self):
        customers = self.customer_model.get_customers()

        if not customers:
            print("No Customers Found")
            return

        headers = ["Customer ID", "Username", "Name", "Email", "Phone"]

        print(tabulate(customers, headers=headers, tablefmt="grid"))

    def DeleteCustomer(self):
        self.ViewAllCustomers()

        try:
            customer_id = int(input("Enter Customer ID to Delete: "))
        except ValueError:
            print("Invalid input! Enter a valid number.")
            return

        confirm = input("Are you sure? (y/n): ")

        if confirm.lower() == "y":
            try:
                self.customer_model.delete_customer(customer_id)
                print("Customer deleted successfully")
            except Exception as e:
                print("Error deleting customer:", e)
        else:
            print("Cancelled")

    def BlockCustomer(self):
        self.ViewAllCustomers()

        try:
            user_id = int(input("Enter User ID to Block: "))
        except ValueError:
            print("Invalid input! Enter a valid number.")
            return

        try:
            self.user_model.block_customer(user_id)
            print("Customer blocked successfully")
        except Exception as e:
            print("Error blocking customer:", e)

