import traceback
import sys
try:
    print sys.argv[1]
except:
    print traceback.format_ex()