import subprocess

def Popen(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    lines = proc.stdout.readlines()
    return lines
