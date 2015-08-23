import mylib
import re

class State:
    def __init__(self):
        pass

    def do(self):
        pass

class LinkState(State):
    def do(self, paras):
        line = paras['line']
        cxt = paras['context']
        if "linkTitle" in line:
            m = re.search("href=.+<", line)
            if m != None:
                line = m.group(0)
                lineArr = line.split("\">")
                cxt.ret.append(lineArr[0].lstrip("href=\""))
                cxt.ret.append(lineArr[1].rstrip("<"))
            cxt.changeState("department")
            

class DepartState(State):
    def do(self, paras):
        line = paras['line']
        cxt = paras['context']
        if "lblDepartment" in line:
            m = re.search(">.+<", line)
            if m != None:             
                cxt.ret.append(m.group(0)[1:-1])
            cxt.changeState("date")

class ParseDate(State):
    def do(self, paras):
        line = paras['line']
        cxt = paras['context']
        if "lblReleaseDate" in line:
            m = re.search(">.+<", line)
            if m != None:
                cxt.ret.append(m.group(0)[1:-1])
            cxt.changeState("link")


class Context:
    def __init__(self):
        self.state_map = {
            'link' : LinkState(),
            'department' : DepartState(),
            'date' : ParseDate(),
            #'description' : Desc(),
        }
        self.state = self.state_map['link']
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

class Kmdn_news:
    def __init__(self, paras):
        self.url = paras['url']
        self.queue = []

    def parse(self):
        cxt = Context()
        data = mylib.myurl(self.url)
        for line in data:
            cxt.do(line)
        
        ret = cxt.result()
        i = 0
        while i < len(ret): 
            try:
                print ret[i]
                print ret[i+1]
                print ret[i+2]
                print ret[i+3]
            except:
                pass
            i += 4


    def start(self):
        self.parse()
