from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def upload():
    _ = request.data  # Discard the data
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Upload Server is Live", 200
