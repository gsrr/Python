import sys
sys.path.append("../")
import mylib
import re

class State:
    def __init__(self):
        pass
    
    def do(self):
        pass


class Desc(State):
    def do(self, paras):
        line = paras['line']
        cxt = paras['context']
        if "Body end" in line:
            cxt.changeState('end')
        else:
            cxt.ret.append(line)

class Image(State):
    def do(self, paras):
        line = paras['line']
        cxt = paras['context']
        if "<br />" in line:
            cxt.changeState('desc')
        else:
           m = re.search("<img.+'", line)
           if m != None:
            cxt.ret.append( m.group(0).split()[1].lstrip('src=').strip("'"))
    

class Start(State):
    def do(self, paras):
        line = paras['line']
        cxt = paras['context']
        if "<!-- Body start  -->" in line:
            cxt.changeState('image')



class End(State):
    def do(self, paras):
        pass
        

class Context:
    def __init__(self):
        self.state_map = {
            'start' : Start(),
            'image' : Image(),
            'desc' : Desc(),
            'end' : End(),
        }
        self.state = self.state_map['start']
        self.ret = []

    def changeState(self, state):
        self.state = self.state_map[state]

    def do(self,line):
        paras = {
            'line' : line,
            'context' : self,
        }
        self.state.do(paras)

    def result(self):
        return self.ret


class Parser:
    def __init__(self, paras):
        self.url = paras['url']

    def parse(self):
        cxt = Context()
        data = mylib.myurl(self.url)
        for line in data:
            cxt.do(line)
        
        ret = cxt.result()
        print ret[0]
        print ret[1]
    def start(self):
        self.parse()



if __name__ == "__main__":
    p = Parser({'url':"http://www.kmdn.gov.tw/ch/News_NewsContent.aspx?NewsID=257780&PageType=0&Language=0&CategoryID=0&DepartmentID=&Keyword="})
    p.start()
