
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
            context.state = context.stateMap['Filing']
            

class FilingState(State):
    def parse(self, line, context):
        if "Filing Date" in line:
            context.result.append( line.split(">")[1].strip("</p"))
            context.state = context.stateMap['Desc']

class DescState(State):
    def parse(self, line, context):
        if "According" in line:
            context.result.append(line)
            context.state = context.stateMap['End']

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
                'Filing':FilingState(),
                'Desc':DescState(),
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
        
        print self.parser.result

def main():
    parser = Context(StartState())
    with open('test.html', 'r') as f:
        data = f.readlines()
        pm = ParserManager(data, parser)
        pm.startParse()

if __name__ == "__main__":
    main()
