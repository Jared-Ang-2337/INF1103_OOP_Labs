from Inventory import Inventory
from FileHandler import FileHandler
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Validator import Validator

db_file = "inventory.json"

class main:
    def __init__(self,file):
        self.__file_name = file
        self.__f = FileHandler(self.__file_name)
        self.__set_inventory()
        self.menu()
        
    def __set_inventory(self):
        self.__product_list, self.__idnum = self.__f.parse_content()
        self.__inventory = Inventory()
        for item in self.__product_list:
            if item["type"] == "physical":
                new_product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item["weight"])
            else:
                new_product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item["size"])
            self.__inventory.add_product(new_product)

    def __add_product(self):
        print("Adding Product")
        name = Validator.get_str("Product Name : ")
        price = Validator.get_float("Price : ")
        stock = Validator.get_int("Stock : ")
        type = Validator.get_choice("Physical(P) or Digital(D) : ",["P","D"])
        self.__idnum += 1
        if type == "P":
            weight = Validator.get_float("Weight : ")
            new_product = PhysicalProduct(self.__idnum,name,price,stock,weight)
        else :
            size = Validator.get_float("Size : ")
            new_product = DigitalProduct(self.__idnum,name,price,stock,size)
        self.__inventory.add_product(new_product)
        print("Successfuly added product.\n")

    def __udpate_product(self):
        print("Update Product Stock")
        self.__inventory.display_all()
        product_id = Validator.get_int("Enter Product ID To Change : ")
        product_stock = Validator.get_int("Enter New Stock Amount : ")
        self.__inventory.update_product(product_id,product_stock)

    def __search_product(self):
        print("Search Product")
        self.__inventory.display_all()
        product_id = Validator.get_int("Enter Product ID to Search For : ")
        self.__inventory.search_product(product_id)

    def menu(self):
        while True:
            print("Inventory handler")
            print("1. Display all Products")
            print("2. Add Product")
            print("3. Update Product Stock")
            print("4. Search Product")
            print("5. Save Inventory")
            print("6. Exit")
            option = Validator.get_int("Option : ",1,6)
            print("\n")

            if option == 1:
                self.__inventory.display_all()

            elif option == 2:
                self.__add_product()

            elif option == 3:
                self.__udpate_product()

            elif option == 4:
                self.__search_product()

            elif option == 5:
                self.__f.close_file(self.__inventory.get_product())
                print("Saved Inventory.")

            elif option == 6:
                self.__f.close_file(self.__inventory.get_product())
                print("Exiting Program.")
                break

app = main(db_file)

