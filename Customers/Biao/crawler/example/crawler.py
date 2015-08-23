import mylib
import myparser
import urllib
import time
import random
import urlparse
import traceback

def readFile(path):
    data = []
    with open(path, "r") as fr:
        lines = fr.readlines()
        for line in lines:
            line = line.strip()
            data.append(line)
    return data


def showResult(fd, index, data):
    ret = [index, data[1], data[0]]
    if "DISMISSED" == data[0]: 
        if "voluntary" in data[2]:
            ret.append("1")
        else:
            ret.append("0")
    else:
        ret.append("0")

    ret.append(data[2])
    print " ".join(ret)
    fd.write(" ".join(ret) + "\n")
    fd.flush()


def extractDataFromURL(data):
    fd = open("./result", "a")
    url_temp="http://securities.stanford.edu/filings-case.html?id=%s"
    for i in range(1, len(data)):
        url_path = url_temp%(data[i])
        print i, url_path,
        url_data = myLib.myUrl(url_path)
        parser = CaseParser.Context(CaseParser.StartState())
        pm = CaseParser.ParserManager(url_data, parser)
        pm.startParse()
        showResult(fd, data[i], pm.result())
        sleep_time = random.randint(1,3)
        time.sleep(sleep_time)
        
    fd.close()

def crawl_webPage(data):
    url_temp="http://securities.stanford.edu/filings-case.html?id=%s"
    for i in range(1, len(data)):
        url_path = url_temp%(data[i])
        print i, url_path
        url_data = myLib.myUrl(url_path)
        with open("./sample/%s"%data[i], "w") as f:
            for line in url_data:
                f.write(line + "\n")

        sleep_time = random.randint(1,3)
        time.sleep(sleep_time)


def debug_list(msg):
    for line in msg:
        print line

def debug(msg):
    t = type(msg)
    if t == list:
        debug_list(msg)


def createObj(title, paras):
    if title == "kmdn_news":
        return myparser.Kmdn_news(paras)

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
            if line:
                title = line.split()[0]
                url = line.split()[1]
                start_crawl(title, url)
    except:
        print traceback.format_exc()


    #crawl_webPage(data)

if __name__ == "__main__":
    main()
