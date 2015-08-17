import os
import sys



lib_path = "../lib"

def libFiles():
	files =  os.walk(lib_path)
	for file in files:
		abs_path = os.path.abspath(file[0])
		for file in file[2]:
			print abs_path + "/" + file		

def readFile(file):
	data = []
	with open(file , "r") as fr:
		lines = fr.readlines()
		for line in lines:
			data.append(line)

	return data


def extractPathAndFile(line):
	lib = line.split()[1]
	path = lib_path + "/" + lib.split(".")[0] + ".py"
	func = "def " + lib.split(".")[1] + "("
	return (path, func)

def importFunc(line):
	codes = []
	path, func = extractPathAndFile(line)
	data = readFile(path)
	code_insert = False
	for line in data:
		print line
		if line.startswith(func):
			code_insert = True
			codes.append(line)
			continue
		if code_insert == True:
			if line.startswith("def"):
				code_insert = False
				break
			codes.append(line)
	return codes

def replaceImportFunc(data):
	new_data = []
	for line in data:
		if line.startswith("#import"):
			new_data += importFunc(line)
		else:
			new_data.append(line)
	
	return new_data


def output(data):
	with open("./tmp.py", "w") as fw:
		for line in data:
			fw.write(line)

def main():
	lib_files = libFiles()
	data = readFile(sys.argv[1])
	new_data = replaceImportFunc(data)
	output(new_data)

	

if __name__ == "__main__":
	main()
