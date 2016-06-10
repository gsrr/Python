import socket
import os

for i in range(254):
	print i
	ip = "192.168.254.%d"%i
	ret = os.system("ping -w 1 %s > /dev/null"%ip)
	if ret == 0:
		print ip
