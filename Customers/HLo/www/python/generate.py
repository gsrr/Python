import sys
import lib
import os
import shutil
import win32Convert
import traceback 
import re


dstDir = ".\\uploads"

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
    
def convertFiles(paths):
    htmls = []
    for path in paths:
        name = os.path.basename(path)
        #win32Convert.convertToHTML(path, dstDir + "\\%s.html"%(name.split(".")[0]))
        abs_path = os.path.abspath(path)
        dst_path = os.path.abspath(dstDir) + "\\%s.html"%(name.split(".")[0])
        win32Convert.convertToHTML(abs_path, dst_path)
        htmls.append(dst_path)
    return htmls

def writeToHtml(path, tr_string):  
    with open(path , "w") as fw:
        fw.write("<html>\n")
        fw.write("<body>\n")
        fw.write("<table>\n")
        fw.write(tr_string)
        fw.write("</table>\n")
        fw.write("</body>\n")
        fw.write("</html>\n")
        
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
     
    writeToHtml(dstDir + "\\subject.html", subject)
    writeToHtml(dstDir + "\\shortAns.html", shortAns)
    writeToHtml(dstDir + "\\detailAns.html", detailAns)
    
def generate(paras):
    outFiles = [dstDir + "\\subject.html", dstDir + "\\shortAns.html" , dstDir + "\\detailAns.html"]
    for outFile in outFiles:
        try:
            os.remove(outFile)
        except:
            pass
    '''
    files = paras["files"].split("@@")
    paths = []
    for file in files:
        paths.append(file.split(";")[2])
    
    clearUploadDir()
    #docFiles = copyFiles(paths)
    htmls = convertFiles(paths)
    '''
    files = os.listdir(dstDir)
    htmls = []
    for file in files:   
        if file.endswith(".html"):
            htmls.append(dstDir + "\\" + file)
    print htmls
    extractTR(htmls)
    
     

def test(paras):
    print "hello world"
    
def main():
    paras = lib.readParas()
    func = getattr(sys.modules[__name__], paras['op'])
    func(paras)
 
if __name__ == "__main__":
    main()