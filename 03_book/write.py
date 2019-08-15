class WhiteIntxt:
    def __init__(self):
        self.__title = None
        self.__content = []
        self.__file = None
    # 章节名
    def set_title(self, title):
        self.__title = title
    # 章节内容
    def set_content(self, content):
        self.__content.append(content)
    def white(self):
        path = r"C:\Users\Administrator\Documents\我的文档\001.txt"
        self.__file = open(path, "a", encoding="utf-8")
        self.__file.write(self.__title)
        self.__file.write("\n")
        for i in self.__content:
            self.__file.write(i)
            self.__file.write("\n")
        self.__file.write("\n")
        print(self.__title)
        self.__title = None
        self.__content = []
    def end(self):
        self.__file.close()