import os
import glob
import sys
import time


def getLibFilePath(libFunc):
	ret =  os.walk("../lib")
	for item in ret:
		abspath = os.path.abspath(item[0])
		for file in item[2]:
			if libFunc == file.rstrip(".l"):	
                                print "find lib file:" + file
				filepath = abspath + "/" + file
				return filepath

def getAllLibPath():
    paths = []
    ret = os.walk("../lib")
    for item in ret:
        for file in item[2]:
            abs_path = os.path.abspath(item[0])
            file_path = abs_path + "/" + file
            paths.append(file_path)

    return paths

def getLibFunc(libFunc):
    ret = ""
    filepath = getLibFilePath(libFunc)
    with open(filepath, "r") as fr:
        lines = fr.readlines()
        for line in lines:
            ret = ret + line
    return ret


def help(args):
    paths = getAllLibPath()
    print "-" * 50
    for path in paths:
        with open(path , "r") as fr:
            lines = fr.readlines()
            for line in lines:
                if "#def" in line:
                    print line.split("::")[1]
                    print

    print "-" * 50
    
def main(args):
    sourceFile = args[1]
    with open(sourceFile, "r") as fr:
        lines = fr.readlines()
        with open("./tmp.py" , "w") as fw:
            for line in lines:
                if line.startswith("#mydef"):
                    libFunc = line.lstrip("#mydef")
                    fw.write(getLibFunc(libFunc.strip()))
                else:
                    fw.write(line)
    
    os.system("python ./tmp.py %s"%(" ".join(args[2:])))


if __name__ == "__main__":
    main(sys.argv[1:])


