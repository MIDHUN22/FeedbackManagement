from Models.db import Database

class ProdctModel:
    def CreateProdct(self):
        print("Creating Product")

    def ViewAllProducts(self):
        db.cursor.execute(
            '''
            SELECT * FROM products
            '''
        )
        products=db.cursor.fetchall()
        return products