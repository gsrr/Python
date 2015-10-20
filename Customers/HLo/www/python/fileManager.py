import lib
import sys
import os
import json

def browseDir(paras):
    dirs = []
    files = os.listdir(paras['path'])
    for file in files:
        path = paras['path'] + file
        if os.path.isdir(path):
            dirs.append(path.decode("big5"))
    #print dirs
    print json.dumps(dirs)
    
def main():
    paras = lib.readParas()
    func = getattr(sys.modules[__name__], paras['op'])
    func(paras)
 
if __name__ == "__main__":
    main()