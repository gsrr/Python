import traceback
import sys
import lib
    
def hello(paras):
    print "Hello World"

def main():
    paras = lib.readParas()
    func = getattr(sys.modules[__name__], paras['op'])
    func(paras)
 
if __name__ == "__main__":
    main()