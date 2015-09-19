import sys
import os
import comtypes.client

wdFormatHTML = 8
wdFormatPDF = 17

def convertToHTML(in_file, out_file):
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat = wdFormatFilteredHTML)
    doc.Close()
    word.Quit()

def convertToPDF(in_file, out_file):
    in_file = os.path.abspath("Original.docx")
    out_file = os.path.abspath("bbb.pdf")

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()