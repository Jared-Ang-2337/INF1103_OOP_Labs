from product import Product


class Inventory:
    """Aggregation: holds references to Products it did not create and does not destroy."""

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: int) -> Product | None:
        """Drop the reference only; the Product object lives on and is returned."""
        product = self.find_product(product_id)
        if product is not None:
            self.__products.remove(product)
        return product

    def find_product(self, product_id: int) -> Product | None:
        for product in self.__products:
            if product.get_productid() == product_id:
                return product
        return None

    def search_product(self, id_num: int) -> None:
        product = self.find_product(id_num)
        if product is None:
            print("Product not found.\n")
        else:
            product.display_information()

    def update_product(self, id_num: int, stock: int) -> None:
        product = self.find_product(id_num)
        if product is None:
            print("Product not found.\n")
        else:
            product.update_stock(stock)

    def get_product(self) -> list[dict]:
        return [item.get_product() for item in self.__products]

    def display_all(self) -> None:
        if self.__products:
            for product in self.__products:
                product.display_information()
            print("")
        else:
            print("No products")
