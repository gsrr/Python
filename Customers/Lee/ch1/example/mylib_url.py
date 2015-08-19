import urllib
import sys

urlPath = "http://securities.stanford.edu/filings-case.html?id=105646"

def webData(urlPath):
        f = urllib.urlopen(urlPath)
        data = f.readlines()
        f.close()
        return data

def browseList(data):
    for line in data:
        print line

def test_browseList():
    global urlPath
    data = webData(urlPath)
    browseList(data)

def main():
    func = getattr(sys.modules[__name__], sys.argv[1])
    func()

if __name__ == "__main__":
    main()
