import product

class physicalProduct(product.product):
    def __init__(self,productid,name,price,stock,weight):
        super().__init__(productid,name,price,stock)
        self.__weight = weight

    def display_information(self):
        print ("Product ID : {id}, Name : {name}, Price : {price}, Stock : {stock}, Weight : {weight}".format(id=self._productid,name=self._name, price=self._price, stock=self._stock, weight=self.__weight))
