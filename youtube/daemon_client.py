#!/usr/bin/env python3
import socket
import json
import sys

SOCKET_PATH = "/tmp/mpg123d.sock"

def send(cmd):
    if not cmd:
        print("usage: daemon_client.py play <url> | stop")
        return

    payload = {}

    if cmd[0] == "play":
        if len(cmd) < 2:
            print("missing url")
            return
        payload = {
            "cmd": "play",
            "url": cmd[1]
        }
    elif cmd[0] == "stop":
        payload = {
            "cmd": "stop"
        }
    else:
        print("unknown command")
        return

    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.connect(SOCKET_PATH)
    s.send(json.dumps(payload).encode())
    resp = s.recv(4096)
    s.close()

    print(resp.decode())

if __name__ == "__main__":
    send(sys.argv[1:])

