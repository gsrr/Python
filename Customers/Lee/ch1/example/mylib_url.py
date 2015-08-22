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

def cleanData(data):
    data_clean = []
    for line in data:
        line = line.strip()
        data_clean.append(line)

    return data_clean

def test_cleanData():
    global urlPath
    data = webData(urlPath)
    data = cleanData(data)
    browseList(data)

def extractStatus(data):
    flag = False
    for line in data:
        if flag == True:
            flag = False
            print line
            lineArr = line.split()
            print lineArr
            return lineArr[-1]

        if "Status" in line:
            flag = True


def test_extractStatus():
    global urlPath
    data = webData(urlPath)
    target_line = ""
    flag = False
    for line in data:
        if flag == True:
            target_line = line
            break
        if "Case Status" in line:
            flag = True
            print line

    line_list = target_line.strip().split(" ") 
    print line_list
    print line_list[-1]
    #data = cleanData(data)
    #print extractStatus(data)
    
    

def main():
    func = getattr(sys.modules[__name__], sys.argv[1])
    func()

if __name__ == "__main__":
    main()
