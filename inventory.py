
from Product import Product

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self,product):
        self.__products.append(product)
        

    def search_product(self,id_num):
        for product in self.__products:
            if product.get_productid() == id_num:
                product.get_
                return product.display_information()
            
        print("Product not found.\n")

    def update_product(self,id_num,stock):
        for product in self.__products:
             if product.get_productid() == id_num:
                product.update_stock(stock)
                return
        print("Product not found.\n")

    def get_product(self):
        product_list = []
        for item in self.__products:
            product_list.append(item.get_product())
        return product_list


    def display_all(self):
        if self.__products:
            for product in self.__products:
                product.display_information()
            print ("")
        else :
            print ("No products")