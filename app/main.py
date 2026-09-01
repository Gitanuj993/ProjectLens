# main logic
from flask import Flask, jsonify, request
from urllib.parse import urlparse


app = Flask(__name__)

def validate_url(url):
    try:
        parsed = urlparse(url)

        return (
            parsed.scheme in ("http", "https")
            and bool(parsed.netloc)
        )
    except Exception:
        return False
    

@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "project-evaluator"
    })

@app.post("/analyze")
def analyze():
    data = request.get_json(silent=True) or {}

    url = data.get("url")

    if not url:
        return jsonify({
            "error": "URL is required"
        }), 400

    if not validate_url(url):
        return jsonify({
            "error": "Invalid URL"
        }), 400

    return jsonify({
        "status": "accepted",
        "url": url,
        "message": "URL received successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
