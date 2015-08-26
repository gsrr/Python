import sys
import os
import comtypes.client

wdFormatFilteredHTML = 10
wdFormatPDF = 17

in_file = os.path.abspath("Original.docx")
out_file = os.path.abspath("output.html")

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
#doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.SaveAs(out_file, FileFormat=wdFormatFilteredHTML)
doc.Close()
word.Quit()