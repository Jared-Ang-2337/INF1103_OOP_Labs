class fileHandler:
    def __init__(self,file):
        self.__file = file
        self.__content = self.__read_file()

    def __read_file(self):
        try:
            with open(self.__file, "r") as file:
                return file.read()
        except FileNotFoundError:
            with open(self.__file, "w") as file:
                pass
            return ""

    def close_file(self,product_list):
        with open(self.__file,"w") as file:
            for row in product_list:
                line = ",".join(str(item) for item in row)
                file.write(line+"\n")

        
    def get_content(self):
        return self.__content


    def parse_content(self):
        new_list = []
        items = self.__content.split("\n")
        if items != ['']:
            for item in items:
                if item != "":
                    new_item = item.split(",")
                    new_list.append(new_item)
            order_num = int(new_list[-1][0])
        else:
            order_num = 1000
        return new_list, order_num



