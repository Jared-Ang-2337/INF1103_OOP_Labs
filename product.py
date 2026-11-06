from abc import ABC, abstractmethod

from supplier import Supplier


class Product(ABC):
    def __init__(self, productid: int, name: str, price: float,
                 stock: int, supplier: Supplier):
        self._productid: int = productid
        self._name: str = name
        self._price: float = price
        self._stock: int = stock
        # Association: Product knows its Supplier but does not own it.
        self._supplier: Supplier = supplier

    @property
    def price(self) -> float:
        return self._price

    @property
    def supplier(self) -> Supplier:
        return self._supplier

    def update_stock(self, quantity: int) -> None:
        """Contract: set stock to `quantity`. Every subclass keeps this meaning."""
        self._stock = quantity

    def display_information(self) -> None:
        print("Product ID : {id}, Name : {name}, Price : {price}, Stock : {stock} ".format(
            id=self._productid, name=self._name, price=self._price, stock=self._stock), end="")

    def display_supplier(self) -> str:
        return self._supplier.display_information()

    def get_productid(self) -> int:
        return self._productid

    def get_product(self) -> dict:
        return {"id": self._productid, "name": self._name,
                "price": self._price, "stock": self._stock,
                "supplier": self._supplier.to_dict()}

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
