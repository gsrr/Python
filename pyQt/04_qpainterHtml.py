import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
 
app = QApplication(sys.argv)
 
web = QWebView()
#web.load(QUrl("http://www.google.com"))
web.load(QUrl("http://ptt-kkman-pcman.org/ptt-web-bbs.html"))

#web.show()
 
printer = QPrinter()
printer.setPageSize(QPrinter.A4)
printer.setOutputFormat(QPrinter.PdfFormat)
printer.setOutputFileName("04_file.pdf")
 
def convertIt():
    web.print_(printer)
    print "Pdf generated"
    QApplication.exit()
 
QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)
 
sys.exit(app.exec_())