class product:
    def __init__(self,productid,name,price,stock):
        self.__productid = productid
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self,quantity):
        self.__stock = quantity

    def display_information(self):
        print ("Product ID : {id}, Name : {name}, Price : {price}, Stock : {stock}".format(id=self.__productid,name=self.__name, price=self.__price, stock=self.__stock))