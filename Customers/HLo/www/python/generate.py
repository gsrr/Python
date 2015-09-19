import sys
import lib
import os
import shutil
import win32Convert
import traceback 
import re
import json


dstDir = ".\\uploads"
tempplateDir = ".\\template"
abs_dstDir = os.path.abspath(dstDir)
abs_template = os.path.abspath(tempplateDir)

templateFiles = [abs_template + "\\QuestionTemplate.docx", abs_template + "\\ShortAnswerTemplate.docx", abs_template + "\\LongAnswerTemplate.docx"]
templateHtml = [abs_dstDir + "\\QuestionTemplate.html", abs_dstDir + "\\ShortAnswerTemplate.html", abs_dstDir + "\\LongAnswerTemplate.html"]

def clearUploadDir():
    dst_path = os.path.abspath(dstDir)
    try:
        shutil.rmtree(dst_path)
        os.mkdir(dst_path)
    except:
        pass
    
    try:
        os.mkdir(dst_path)
    except:
        pass
    
    
def copyFiles(paths):
    docFiles = []
    for path in paths:
        name = os.path.basename(path)
        dst = dstDir + "\\%s"%name
        shutil.copyfile(path, dst)
        docFiles.append(dst)
    return docFiles
    
def convertFiles(paras):
    paths = paras['paths']
    paths += templateFiles
    htmls = []
    for path in paths:
        name = os.path.basename(path)
        #win32Convert.convertToHTML(path, dstDir + "\\%s.html"%(name.split(".")[0]))
        abs_path = os.path.abspath(path)
        dst_path = os.path.abspath(dstDir) + "\\%s.html"%(name.split(".")[0])
        win32Convert.convertToHTML(abs_path, dst_path)
        htmls.append(dst_path)
        
    return htmls

def writeToHtml(templateFile, path, tr_string): 
    print templateFile
    with open(path , "w") as fw:
        with open(templateFile, "r") as fr:
            lines = fr.readlines()
            ignore = False
            for line in lines:
                if "<table" in line:
                    fw.write(line)
                    fw.write(tr_string)
                    ignore = True
                    continue
                if "</table>" in line:
                    fw.write(line)
                    ignore = False
                    continue
                
                if not ignore:
                    fw.write(line)

        
def extractTR(htmls):
    subject = ""
    shortAns = ""
    detailAns = ""
    index = 0
    for html in htmls:
        index += 1
        td_index = str("<td>%d</td>\n"%index)
        with open(html, "r") as fr:
            data = fr.read()
            items = re.findall(r'<tr>(.*?)</tr>', data , re.M|re.I|re.S)
            # for item in items:
                # print "<tr>\n" + item + "</tr>\n"
            # break
            subject += "<tr>\n" + td_index + items[1] + "</tr>\n"
            shortAns += "<tr>\n"+ td_index + items[2] + "</tr>\n"
            detailAns += "<tr>\n"+ td_index + items[3] + "</tr>\n"
     
    writeToHtml(templateHtml[0], dstDir + "\\question.html", subject)
    writeToHtml(templateHtml[1], dstDir + "\\shortAnswer.html", shortAns)
    writeToHtml(templateHtml[2], dstDir + "\\LongAnswer.html", detailAns)
    return 0


def getHtmlFromPath(paths):
    htmls = []
    for path in paths:
        name = os.path.basename(path)
        dst_path = os.path.abspath(dstDir) + "\\%s.html"%(name.split(".")[0])
        htmls.append(dst_path)
    return htmls
    
def generate(paras):
    outFiles = [dstDir + "\\subject.html", dstDir + "\\shortAns.html" , dstDir + "\\detailAns.html"]
    for outFile in outFiles:
        try:
            os.remove(outFile)
        except:
            pass
    
    
    paths = paras['paths']
    #clearUploadDir()
    #docFiles = copyFiles(paths)
    htmls = getHtmlFromPath(paths)
    '''
    files = os.listdir(dstDir)
    htmls = []
    for file in files:   
        if file.endswith(".html"):
            htmls.append(dstDir + "\\" + file)
    print htmls
    '''
    ret = extractTR(htmls)
    if ret == 0:
        print json.dumps(outFiles)
    else:
        print "error"
     

def test(paras):
    print "hello world"
    
def main():
    paras = lib.readParas()
    files = paras["files"].split("@@")
    paths = []
    for file in files:
        paths.append(file.split(";")[2])
    paras['paths'] = paths
    func = getattr(sys.modules[__name__], paras['op'])
    func(paras)
 
if __name__ == "__main__":
    main()