from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    def __init__(self, productid: int, name: str, price: float,
                 stock: int, download_size: float, supplier: Supplier):
        super().__init__(productid, name, price, stock, supplier)
        self.__size: float = download_size

    def display_information(self) -> None:
        super().display_information()
        print("Download Size : {size} MB".format(size=self.__size))

    def get_fulfilment_info(self) -> str:
        return "This is a Digital Product that is delivered digitally."

    def get_product(self) -> dict:
        data = super().get_product()
        data.update({"type": "digital", "size": self.__size})
        return data
