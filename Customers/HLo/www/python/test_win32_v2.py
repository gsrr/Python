from win32com import client as wc
word = wc.Dispatch('Word.Application')
doc = word.Documents.Open('Original.docx')
doc.SaveAs('aaa.html', 8)
doc.Close()
word.Quit()