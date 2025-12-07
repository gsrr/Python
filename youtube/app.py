import os
import json
import socket
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# =========================
# 設定
# =========================
SOCKET_PATH = "/tmp/mpg123d.sock"
OUTPUT_FILE = "/tmp/output"


MAP_FILE = "downloads.json"

def load_map():
    if not os.path.exists(MAP_FILE):
        return {}
    with open(MAP_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# =========================
# IPC helper
# =========================
def send_daemon(payload: dict):
    if not os.path.exists(SOCKET_PATH):
        return {"ok": False, "error": "daemon not running"}

    try:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect(SOCKET_PATH)
        s.send(json.dumps(payload).encode())
        resp = s.recv(8192)
        s.close()
        return json.loads(resp.decode())
    except Exception as e:
        return {"ok": False, "error": str(e)}

# =========================
# 頁面
# =========================
@app.route("/")
def index():
    return render_template("index.html")

# =========================
# API: 播放
# =========================
@app.route("/api/play", methods=["POST"])
def api_play():
    data = request.get_json(silent=True) or {}

    url = data.get("yurl")
    print("play:", url)

    if not url:
        return jsonify({"ok": False, "error": "missing url"}), 400

    return jsonify(send_daemon({
        "cmd": "play",
        "url": url,
    }))


# =========================
# API: 停止
# =========================
@app.route("/api/stop", methods=["POST"])
def api_stop():
    return jsonify(send_daemon({
        "cmd": "stop"
    }))

# =========================
# API: 讀取 mpg123 / yt-dlp output
# =========================
@app.route("/api/read_output")
def api_read_output():
    if not os.path.exists(OUTPUT_FILE):
        return jsonify({
            "content": "",
            "size": 0
        })

    try:
        with open(OUTPUT_FILE, "r", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        return jsonify({
            "content": "",
            "size": 0,
            "error": str(e)
        })

    return jsonify({
        "content": content,
        "size": len(content)
    })

@app.route("/api/list", methods=["GET"])
def api_list():
    mapping = load_map()

    result = sorted(
        mapping.values(),
        key=lambda x: x.get("timestamp", 0),
        reverse=True
    )

    sanitized = []
    for item in result:
        sanitized.append({
            "vid": item.get("vid"),
            "title": item.get("title"),
            "url": item.get("url"),
        })

    return jsonify(sanitized)


# =========================
# 啟動
# =========================
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8888,
        debug=True
    )

