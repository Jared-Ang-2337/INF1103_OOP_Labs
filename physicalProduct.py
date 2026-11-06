from product import Product
from canBeShipped import CanBeShipped
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, productid: int, name: str, price: float,
                 stock: int, weight: float, supplier: Supplier):
        super().__init__(productid, name, price, stock, supplier)
        self.__weight: float = weight

    def display_information(self) -> None:
        super().display_information()
        print("Weight : {weight}kg".format(weight=self.__weight))

    def get_fulfilment_info(self) -> str:
        return "This is a Physical Product that requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 2

    def get_product(self) -> dict:
        data = super().get_product()
        data.update({"type": "physical", "weight": self.__weight})
        return data
