from product import Product


class OrderLine:
    """Part of an Order (composition). Refers to a Product but does not own it."""

    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity


class Order:
    """Whole in a composition: creates, manages and discards its own OrderLines."""

    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        self.order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, product_id: int) -> bool:
        for line in self.order_lines:
            if line.product.get_productid() == product_id:
                self.order_lines.remove(line)
                return True
        return False

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.order_lines)

    def display_order(self) -> None:
        print("Order {}".format(self.order_id))
        for line in self.order_lines:
            print("  {} x{} = ${:.2f}".format(
                line.product.get_productid(), line.quantity, line.calculate_subtotal()))
        print("  Total: ${:.2f}".format(self.calculate_total()))
