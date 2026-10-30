from Product import Product

class DigitalProduct(Product):
    def __init__(self,productid,name,price,stock,download_size):
        super().__init__(productid,name,price,stock)
        self.__size = download_size

    def display_information(self):
        super().display_information()
        print("Download Size : {size} MB".format(size = self.__size))

    def get_fulfilment_info(self):
        print("This is a Digital Product that is delivered digitally.")

    def get_product(self):
        return {"type": "digital", "id": self._productid, "name": self._name,
            "price": self._price, "stock": self._stock, "size": self.__size}
