import time

class State:
    def __init__(self):
        pass

    def parse(self, line, context):
        pass

class StartState(State):
    def __init__(self):
        pass

    def parse(self, line, context):
        if "Case Status" in line:
            context.state = context.stateMap['Status'] 
            context.state.parse(line, context)

class StatusState(State):
    def parse(self, line, context):
        if "icon-check" in line:
            context.result.append( line.split()[-1])
            context.state = context.stateMap['Around']
            

class AroundState(State):
    def parse(self, line, context):
        if "On or around" in line:
            context.result.append( line.split()[3])
            context.state = context.stateMap['Desc']

class ExtractState(State):
    def parse(self, line, context):
        context.result.append( line.strip().replace("<br/>", ""))
        context.state = context.stateMap['End']

class DescState(State):
    def parse(self, line, context):
        if "span12" in line:
            context.state = context.stateMap['Extract']
            extract = True


class EndState(State):
    def parse(self, line, context):
        pass

class Context(State):
    def __init__(self, state, stateMap =None):
        self.state = state
        #self.stateMap = stateMap
        self.stateMap={
                'Start':StartState(),
                'Status':StatusState(),
                'Around':AroundState(),
                'Desc':DescState(),
                'Extract':ExtractState(),
                'End':EndState(),
        }
        self.result = []
    
    def parse(self, line):
        self.state.parse(line, self)
    
    def result(self):
        return self.result

class ParserManager:
    def __init__(self, data, parser):
        self.data = data
        self.parser = parser

    def startParse(self):
        for line in self.data:
            self.parser.parse(line)
        
    def result(self):
        return self.parser.result


def main():
    parser = Context(StartState())
    with open('test.html', 'r') as f:
        data = f.readlines()
        pm = ParserManager(data, parser)
        pm.startParse()
        print pm.result()

if __name__ == "__main__":
    main()
