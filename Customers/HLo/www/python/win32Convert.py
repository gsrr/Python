#import win32com.client as win32
import win32com.client
import traceback

def convertToHTML(in_file, out_file):
    print in_file, out_file
    wordapp = win32com.client.gencache.EnsureDispatch("Word.Application.8")
    try:
        wordapp.Documents.Open(in_file)
        #wordapp.ActiveDocument.SaveAs(out_file, FileFormat=win32com.client.constants.wdFormatFilteredHTML)
        wordapp.ActiveDocument.SaveAs(out_file, FileFormat=win32com.client.constants.wdFormatHTML)
        wordapp.ActiveDocument.Close()
    except:
        pass
    finally:
        wordapp.Quit()
