from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        _ = request.get_data()
        return "OK", 200
    return "Upload Server is Live 🚀", 200

@app.route("/download")
def download():
    try:
        size_mb = int(request.args.get("size", 10))  # default: 10MB
    except (ValueError, TypeError):
        size_mb = 10

    chunk = b'x' * 1024  # 1KB
    total_chunks = size_mb * 1024  # MB to KB

    def generate():
        for _ in range(total_chunks):
            yield chunk

    return Response(generate(), content_type='application/octet-stream')
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
