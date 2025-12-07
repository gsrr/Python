#!/usr/bin/env python3
import os
import socket
import signal
import tempfile
import os, json, time, subprocess

SOCKET_PATH = "/tmp/mpg123d.sock"
DOWNLOAD_DIR = "downloads"
OUTPUT_FILE = "/tmp/output"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

mpg_proc = None

# -------------------------
def cleanup():
    if os.path.exists(SOCKET_PATH):
        os.remove(SOCKET_PATH)



DOWNLOAD_DIR = "downloads"
MAP_FILE = "downloads.json"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def load_map():
    if not os.path.exists(MAP_FILE):
        return {}
    with open(MAP_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_map(data):
    with open(MAP_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def fetch_metadata(url):
    cmd = [
        "yt-dlp",
        "-j",
        "--no-warnings",
        "--extractor-args", "youtube:player_js_version=actual",
        url
    ]

    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

    if proc.returncode != 0 or not proc.stdout:
        return None

    info = json.loads(proc.stdout)

    return {
        "vid": info.get("id"),
        "title": info.get("title"),
        "duration": info.get("duration"),
        "uploader": info.get("uploader"),
        "thumbnail": info.get("thumbnail"),
    }

def download(url, vid):
    path = os.path.join(DOWNLOAD_DIR, f"{vid}.mp3")
    mapping = load_map()

    if os.path.exists(path):
        return True, path

    open(OUTPUT_FILE, "w").close()
    meta = fetch_metadata(url)
    print(meta)

    cmd = (
        f'yt-dlp -x --audio-format mp3 '
        f'--no-check-certificate '
        f'--extractor-args youtube:player_js_version=actual '
        f'-o "{path}" "{url}" '
        f'> {OUTPUT_FILE} 2>&1'
    )

    proc = subprocess.Popen(cmd, shell=True)
    ret = proc.wait()

    if ret == 0:
        mapping[vid] = {
            "vid": vid,
            "title": meta.get("title"), 
            "url": url,
            "path": path,
            "timestamp": int(time.time())
        }
        save_map(mapping)
        return True, path

    return False, path


# -------------------------
def play_url(url):
    global mpg_proc

    vid = vid = url.split("v=")[1].split("&")[0]
    path = os.path.join(DOWNLOAD_DIR, f"{vid}.mp3")

    open(OUTPUT_FILE, "w").close()

    ok, path = download(url, vid)
    if not ok:
        return {"ok": False, "error": "download failed"}

    if mpg_proc and mpg_proc.poll() is None:
        mpg_proc.terminate()

    cmd = f"mpg123 -v {path} > {OUTPUT_FILE} 2>&1"
    print(cmd)
    mpg_proc = subprocess.Popen(cmd, shell=True)

    return {"ok": True, "url": url}

# -------------------------
def stop():
    global mpg_proc
    if mpg_proc and mpg_proc.poll() is None:
        mpg_proc.terminate()
        return {"ok": True}
    return {"ok": False, "error": "nothing playing"}

# -------------------------
def handle(msg):
    try:
        data = json.loads(msg)
    except:
        return {"ok": False, "error": "bad json"}

    cmd = data.get("cmd")
    if cmd == "play":
        return play_url(data.get("url"))
    if cmd == "stop":
        return stop()

    return {"ok": False, "error": "unknown command"}

# -------------------------
def main():
    cleanup()
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(SOCKET_PATH)
    sock.listen(1)

    print("🎵 mpg123 daemon started")

    while True:
        conn, _ = sock.accept()
        msg = conn.recv(8192).decode()
        resp = handle(msg)
        conn.send(json.dumps(resp).encode())
        conn.close()

# -------------------------
if __name__ == "__main__":
    signal.signal(signal.SIGTERM, lambda *_: exit(0))
    main()

