# 下载模块
import requests
import threading

class RequestDelegate:
    def receive_data(self, data): pass

# 数据下载类
class RequestBook(threading.Thread):
    def __init__(self, delegate: RequestDelegate):
        super().__init__()
        self.__delegate = delegate
    def request(self, url):
        ret = requests.get(url)
        data = ret.content.decode("GBK", "ignore")
        self.__delegate.receive_data(data)
