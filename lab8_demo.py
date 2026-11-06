"""Lab 8 demonstration: association, aggregation, composition, LSP, polymorphism."""
from supplier import Supplier
from physicalProduct import PhysicalProduct
from digitalProduct import DigitalProduct
from product import Product
from inventory import Inventory
from order import Order


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def section(title: str) -> None:
    print("\n=== " + title + " ===")


section("2. Association: Supplier <-> Product")
supplier = Supplier("S001", "Acme Supply Co", "sales@acme.example")
mouse = PhysicalProduct(1001, "Mouse", 20.0, 100, 1.0, supplier)
game = DigitalProduct(1002, "GTA6", 100.0, 321, 12.0, supplier)
print(mouse.display_supplier())
print(game.display_supplier())
print("Same Supplier object shared:", mouse.supplier is game.supplier)
del supplier
print("After `del supplier`, product still shows:", mouse.display_supplier())

section("3. Aggregation: Inventory <> Product")
inv_a, inv_b = Inventory(), Inventory()
inv_a.add_product(mouse)
removed = inv_a.remove_product(1001)
print("Removed from A, same object returned:", removed is mouse)
print("Still usable:", mouse.get_fulfilment_info())
inv_b.add_product(mouse)
print("Found in B:", inv_b.find_product(1001) is mouse, "| Missing in A:", inv_a.find_product(1001))

section("4. Composition: Order <> OrderLine")
keyboard = PhysicalProduct(1003, "Keyboard", 150.0, 5, 2.1, mouse.supplier)
order1, order2 = Order("O-1"), Order("O-2")
order1.add_order_line(mouse, 2)
order1.add_order_line(game, 1)
order2.add_order_line(mouse, 5)
order1.display_order()
order2.display_order()
l1, l2 = order1.order_lines[0], order2.order_lines[0]
print("Same Product object in both lines:", l1.product is l2.product)
print("Distinct OrderLine objects:", l1 is not l2)
order1.remove_order_line(1002)
print("After removing a line, Order 1 total:", order1.calculate_total(),
      "| product still alive:", game.get_productid())

section("6/7. LSP and polymorphism")
inv = Inventory()
for p in (mouse, game, keyboard):
    inv.add_product(p)
for p in (mouse, game):
    show_product_details(p)
inv.update_product(1002, 50)       # update_stock works on every Product subtype
inv.update_product(1001, 90)
for item in inv.get_product():
    print(item["type"], item["id"], "stock =", item["stock"])
