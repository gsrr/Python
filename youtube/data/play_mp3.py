import sys
from playsound import playsound

if len(sys.argv) < 2:
    print("用法: python play_mp3.py <檔案>")
else:
    playsound(sys.argv[1])

