import mylib
import urllib
import time
import random
import urlparse
import traceback
from myparser import kmdn_news
from myparser import kmdn_weather
from myparser import kmdn_radar

def readFile(path):
    data = []
    with open(path, "r") as fr:
        lines = fr.readlines()
        for line in lines:
            line = line.strip()
            data.append(line)
    return data


def debug_list(msg):
    for line in msg:
        print line

def debug(msg):
    t = type(msg)
    if t == list:
        debug_list(msg)


def createObj(title, paras):
    if title == "kmdn_news":
        return kmdn_news.Kmdn_news(paras)
    elif title == "kmdn_weather":
        return kmdn_weather.Kmdn_weather(paras)
    elif title == "kmdn_radar":
        return kmdn_radar.Kmdn_radar(paras)

def start_crawl(title, url):
    #print urlparse.urljoin(url , "../aaa")
    paras = {
        'title' : title,
        'url': url,
    }
    class_obj = createObj(title, paras)
    class_obj.start()
    
def main():
    try:
        data = readFile("./webpage.cfg")
        debug(data)
        for line in data:
            line = line.strip()
            if line and line[0] != "#":
                title = line.split()[0]
                url = line.split()[1]
                start_crawl(title, url)
    except:
        print traceback.format_exc()


    #crawl_webPage(data)

if __name__ == "__main__":
    main()
