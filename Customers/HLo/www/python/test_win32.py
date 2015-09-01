#import win32com.client as win32
import win32com.client

wordapp = win32com.client.gencache.EnsureDispatch("Word.Application.8")
try:
    wordapp.Documents.Open('Original.docx')
    wordapp.ActiveDocument.SaveAs('11.html', FileFormat=win32com.client.constants.wdFormatFilteredHTML)
    wordapp.ActiveDocument.Close()
finally:
    wordapp.Quit()
