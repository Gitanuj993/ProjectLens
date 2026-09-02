# main logic
from flask import Flask, jsonify, request
from urllib.parse import urlparse

from app.fetcher import fetch_url
from app.detector import detect_source

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
    
@app.get("/")
def home():
    return jsonify({
        "status": "ok",
        "service": "project-evaluator"
    })
    
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

    try:
        result = fetch_url(url)
        source_type = detect_source(url)

        return jsonify({
            "status": "success",
            "url": url,
            "source_type": source_type,
            "fetch": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
