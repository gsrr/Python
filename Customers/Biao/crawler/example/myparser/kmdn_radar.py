import mylib
import re
import ast
import urlparse

class Parser:
    def __init__(self, paras):
        self.url = paras['url']
        self.queue = []

    def parse(self):
        data = mylib.myurl(self.url)
        data[0] = data[0].split("=")[1].strip()
        data[-1] = data[-1].strip(";")
        data_str = "".join(data)
        #print ast.literal_eval(data_str)
        data_image =  data[1].split(":")[0].strip("\"")
        print urlparse.urljoin(self.url, data_image)

        
    def start(self):
        self.parse()
