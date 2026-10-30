import json


class fileHandler:
    def __init__(self, file):
        self.__file = file
        self.__content = self.__read_file()

    def __read_file(self):
        try:
            with open(self.__file, "r") as file:
                text = file.read()
        except FileNotFoundError:
            self.close_file([])
            return []
        if not text.strip():
            return []
        return json.loads(text)

    def close_file(self, product_list):
        with open(self.__file, "w") as file:
            json.dump(product_list, file, indent=2)

    def get_content(self):
        return self.__content

    def parse_content(self):
        new_list = list(self.__content)
        order_num = int(new_list[-1][0]) if new_list else 1000
        return new_list, order_num



