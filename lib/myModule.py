
def loadModules(path):
    Modules = {}
    names = []
    files = os.listdir(path)
    for file in files:
        if file.endswith(".py") and file != "__init__.py":
            name = file.split(".")[0]
            names.append(name)
            Modules[name] = map(__import__, [name])
    return Modules
