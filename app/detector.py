from urllib.parse import urlparse


def detect_source(url):
    parsed = urlparse(url)
    hostname = parsed.netloc.lower()

    if hostname == "github.com" or hostname.endswith(".github.com"):
        return "github"

    if parsed.scheme in ("http", "https"):
        return "website"

    return "unknown"


