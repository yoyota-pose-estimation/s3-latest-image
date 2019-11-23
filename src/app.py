from flask import Flask, request
from s3 import get_latest_images

app = Flask(__name__)


@app.route("/health")
def health():
    return "ok"


@app.route("/api/path/prefix/<path:path_prefix>")
def images(path_prefix):
    return get_latest_images(path_prefix, request.args.get("time"))

