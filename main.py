import product
import inventory
import fileHandler

db_file = "inventory.txt"

class main:
    def __init__(self,file):
        self.__file_name = file
        self.__f = fileHandler.fileHandler(self.__file_name)
        self.__set_inventory()
        self.menu()
        
    def __set_inventory(self):
        self.__product_list, self.__idnum = self.__f.parse_content()
        self.__inventory = inventory.inventory()
        for item in self.__product_list:
            new_product = product.product(item[0],int(item[1]),int(item[2]),int(item[3]))
            self.__inventory.add_product(new_product)

    def __add_product(self):
        print("Adding Product")
        name = input("Product Name : ")
        price = input("Price : ")
        stock = input("Stock : ")
        self.__idnum += 1
        new_product = product.product(self.__idnum,name,price,stock)
        self.__inventory.add_product(new_product)
        print("Successfulyy added product.\n")

    def __udpate_product(self):
        print("Update Product Stock")
        self.__inventory.display_all()
        product_id = int(input("Enter Product ID To Change : "))
        product_stock = int(input("Enter New Stock Amount : "))
        self.__inventory.update_product(product_id,product_stock)

    def __search_product(self):
        print("Search Product")
        self.__inventory.display_all()
        product_id = int(input("Enter Product ID to Search For : "))
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
            option = int(input("Option : "))
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

