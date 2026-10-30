import product

class physicalProduct(product.product):
    def __init__(self,productid,name,price,stock,weight):
        super().__init__(productid,name,price,stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print("Weight : {weight}kg".format(weight=self.__weight))
