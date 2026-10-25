
from . import product

class inventory:
    def __init__(self):
        self.__products = {}
        self.__product_count = 0

    def add_product(self,product):
        id_num = self.__product_count
        self.__product_count += 1
        self.__products[id_num] = product
        

    def search_product(self,id_num):
        product = self.__products[id_num]
        product.display_information

    def display_all(self):
        for product in self.__product_list:
            product.display_information()