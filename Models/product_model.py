from Models.db import db
class ProdctModel:
    def CreateProdct(self,name,category):
        db.cursor.execute(
            ''' 
            SELECT product_id  FROM products where product_name=?
            ''',(name,)
        )
        product=db.cursor.fetchone()
        if product:
            print('Product Already Exist!! Try Different Name!!')
            return
        db.cursor.execute(
            '''
            INSERT INTO products (product_name,category) VALUES(?,?)
            ''',(name,category)
        )
        db.conn.commit()
    def ViewAllProducts(self):
        db.cursor.execute(
            '''
            SELECT * FROM products
            '''
        )
        products=db.cursor.fetchall()
        return products