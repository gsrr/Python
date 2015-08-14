import myLib
import urllib




def extractID(line):
    return line.strip().split()[0]


def readFile(func):
    data = []
    with open("Lien_Data_20150812.txt", "r") as fr:
        line = fr.readline()
        while line:
            data.append(func(line))
            line = fr.readline()
    return data

def extractDataFromURL(data):
    url_temp="http://securities.stanford.edu/filings-case.html?id=%s"
    for i in range(1, len(data)):
        url_path = url_temp%(data[i])
        print url_path
        url_data = myLib.myUrl(url_path)
        for line in url_data:
             print line
        break

        

def main():
    data = readFile(extractID);
    extractDataFromURL(data)

if __name__ == "__main__":
    main()
