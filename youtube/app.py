import subprocess, threading, time, os, re, hashlib, tempfile, shutil
from collections import deque
from flask import Flask, request, render_template, redirect, url_for
import yt_dlp

app = Flask(__name__)

now_playing = ""
now_url = ""
now_thumbnail = ""
proc = None
queue = deque()  # 存 song dict
lock = threading.Lock()

SONGS_FILE = "songs.txt"
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ========= Helpers =========

def title_hash(title: str, length: int = 12) -> str:
    h = hashlib.sha1(title.encode("utf-8")).hexdigest()
    return h[:length]

def get_info(url):
    with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info.get("title", url)
        thumbnail = info.get("thumbnail", "")
        return title, thumbnail

def _read_songs_raw():
    if not os.path.exists(SONGS_FILE):
        return []
    with open(SONGS_FILE, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def _write_songs_raw(lines):
    tmp = SONGS_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    os.replace(tmp, SONGS_FILE)

def load_songs():
    raw = _read_songs_raw()
    songs = []
    for line in raw:
        parts = line.split("|", 3)
        if len(parts) == 4:
            url, title, thumbnail, h = parts
            songs.append({"url": url, "title": title, "thumbnail": thumbnail, "hash": h})
    return songs

def save_song(url, title, thumbnail):
    songs = load_songs()
    for s in songs:
        if s["url"] == url:
            return
    h = title_hash(title)
    with open(SONGS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{url}|{title}|{thumbnail}|{h}\n")

def find_song_by_url(url):
    for s in load_songs():
        if s["url"] == url:
            return s
    return None

def local_mp3_path_by_hash(h: str) -> str:
    return os.path.join(DOWNLOAD_DIR, f"{h}.mp3")

def local_exists(h: str) -> bool:
    return os.path.exists(local_mp3_path_by_hash(h))

# ========= Playback =========

def start_play(url):
    global proc, now_playing, now_url, now_thumbnail
    song = find_song_by_url(url)
    if not song:
        song = {"url": url, "title": url, "thumbnail": "", "hash": title_hash(url)}

    mp3_path = local_mp3_path_by_hash(song["hash"])
    if local_exists(song["hash"]):
        proc = subprocess.Popen(["mpg123", mp3_path])
    else:
        ytdlp = subprocess.Popen(["yt-dlp", "-f", "bestaudio", "-o", "-", url], stdout=subprocess.PIPE)
        ffmpeg = subprocess.Popen(["ffmpeg", "-i", "pipe:0", "-f", "mp3", "-"], stdin=ytdlp.stdout, stdout=subprocess.PIPE)
        proc = subprocess.Popen(["mpg123", "-"], stdin=ffmpeg.stdout)

    now_playing = song["title"]
    now_url = song["url"]
    now_thumbnail = song["thumbnail"]

def monitor_process():
    global proc, now_playing, now_url, now_thumbnail
    while True:
        time.sleep(2)
        with lock:
            if proc and proc.poll() is not None:
                proc = None
                now_playing = ""
                now_url = ""
                now_thumbnail = ""
                if queue:
                    next_song = queue.popleft()
                    start_play(next_song["url"])

# ========= Routes =========

@app.route("/")
def index():
    songs = load_songs()
    downloaded_hashes = {os.path.splitext(f)[0] for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".mp3")}
    return render_template("index.html",
        now_playing=now_playing,
        now_url=now_url,
        now_thumbnail=now_thumbnail,
        queue=list(queue),
        songs=songs,
        downloaded_hashes=downloaded_hashes
    )

@app.route("/play", methods=["POST"])
def play():
    global proc
    url = request.form.get("url")
    with lock:
        if proc and proc.poll() is None:
            if url != now_url:
                song = find_song_by_url(url)
                if song:
                    queue.append(song)
        else:
            start_play(url)
    return redirect(url_for("index"))

@app.route("/add", methods=["POST"])
def add_to_queue():
    url = request.form.get("url")
    title, thumbnail = get_info(url)
    save_song(url, title, thumbnail)
    song = find_song_by_url(url)
    with lock:
        queue.append(song)
    return redirect(url_for("index"))

@app.route("/add_from_saved", methods=["POST"])
def add_from_saved():
    url = request.form.get("url")
    song = find_song_by_url(url)
    if song:
        with lock:
            queue.append(song)
    return redirect(url_for("index"))

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")
    title, thumbnail = get_info(url)
    save_song(url, title, thumbnail)
    song = find_song_by_url(url)
    out_mp3 = local_mp3_path_by_hash(song["hash"])
    if os.path.exists(out_mp3):
        return redirect(url_for("index"))

    with tempfile.TemporaryDirectory() as td:
        tmp_noext = os.path.join(td, "dl_audio")
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": tmp_noext,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "quiet": True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for fn in os.listdir(td):
            if fn.lower().endswith(".mp3"):
                shutil.move(os.path.join(td, fn), out_mp3)
                break

    return redirect(url_for("index"))

@app.route("/remove", methods=["POST"])
def remove_song():
    url = request.form.get("url")
    songs = load_songs()
    songs = [s for s in songs if s["url"] != url]
    lines = [f"{s['url']}|{s['title']}|{s['thumbnail']}|{s['hash']}" for s in songs]
    _write_songs_raw(lines)
    return redirect(url_for("index"))

@app.route("/remove_from_queue", methods=["POST"])
def remove_from_queue():
    url = request.form.get("url")
    with lock:
        for s in list(queue):
            if s["url"] == url:
                queue.remove(s)
                break
    return redirect(url_for("index"))

@app.route("/stop", methods=["POST"])
def stop():
    global proc, now_playing, now_url, now_thumbnail
    with lock:
        if proc and proc.poll() is None:
            proc.kill()
            proc.wait(timeout=1)
        proc = None
        now_playing = ""
        now_url = ""
        now_thumbnail = ""
    return redirect(url_for("index"))

if __name__ == "__main__":
    threading.Thread(target=monitor_process, daemon=True).start()
    app.run(host="0.0.0.0", port=8888, debug=True)

