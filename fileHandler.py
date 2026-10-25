class fileHandler:
    def __init__(self,file):
        self.__file = file
        self.__content = self.__read_file

    def __read_file(self):
        try:
            with open(self.__file, "r") as file:
                return file.read()
        except FileNotFoundError:
            with open(self.__file, "w") as file:
                pass
            return ""

    def __write_file(self):
        with open(self.__file,"w") as file:
            file.write(self.__content)

        
    def get_content(self):
        return self.__content

    def add_content(self,content):
        self.__content.append(content)

    def close_file(self):
        self.__write_file()

