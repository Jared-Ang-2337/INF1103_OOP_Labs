from Product import Product
from CanBeShipped import CanBeShipped

class PhysicalProduct(Product,CanBeShipped):
    def __init__(self,productid,name,price,stock,weight):
        super().__init__(productid,name,price,stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print("Weight : {weight}kg".format(weight=self.__weight))

    def get_fulfilment_info(self):
        print("This is a Physical Product that requires physical shipping.")

    def calculate_shipping_cost(self):
        cost = self.__weight * 2
        print("Shipping cost : ${cost}".format(cost))
        return cost

    def get_product(self):
        return {"type": "physical", "id": self._productid, "name": self._name,
            "price": self._price, "stock": self._stock, "weight": self.__weight}
