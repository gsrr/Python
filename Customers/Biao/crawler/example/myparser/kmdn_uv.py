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
        image_line = ""
        for line in data:
            if "USEMAP" in line:
                image_line = line
                break
        image_str = image_line.split()[1].split("=")[1].strip("\"")
        print urlparse.urljoin(self.url, image_str)
        
    def start(self):
        self.parse()
