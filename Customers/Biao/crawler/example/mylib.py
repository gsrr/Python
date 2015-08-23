import urllib
import sys

def myurl(urlPath):
        data = []
        f = urllib.urlopen(urlPath)
        line = f.readline()
        while line:
            data.append(line.strip())
            line = f.readline()
        f.close()
        return data


def test_myurl():
    #data = myurl("http://www.kmdn.gov.tw/ch/News_NewsList.aspx")
    #data = myurl("http://www.cwb.gov.tw/V7/observe/real/46711.htm")
    data = myurl("http://www.cwb.gov.tw/V7/observe/radar/")
    for line in data:
        print line

            


if __name__ == "__main__":
    func = getattr(sys.modules[__name__], sys.argv[1]) 
    func()
    
