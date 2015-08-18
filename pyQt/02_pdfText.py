from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)

text_file_path = open('02_sample.txt').read()
doc = QTextDocument(text_file_path)

printer = QPrinter(QPrinter.HighResolution)
printer.setOutputFormat(QPrinter.PdfFormat)
printer.setOutputFileName('02_sample.pdf')

doc.print_(printer)