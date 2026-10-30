class product:
    def __init__(self,productid,name,price,stock):
        self._productid = productid
        self._name = name
        self._price = price
        self._stock = stock

    def update_stock(self,quantity):
        self._stock = quantity

    def display_information(self):
        print ("Product ID : {id}, Name : {name}, Price : {price}, Stock : {stock}".format(id=self._productid,name=self._name, price=self._price, stock=self._stock))

    def get_productid(self):
        return self._productid

    def get_product(self):
        return [self._productid, self._name, self._price, self._stock]