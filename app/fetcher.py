from urllib.request import Request, urlopen


def fetch_url(url):
    request = Request(
        url,
        headers={
            "User-Agent": "ProjectLens/1.0"
        }
    )

    with urlopen(request, timeout=10) as response:
        content = response.read()

    return {
        "status_code": response.status,
        "content_type": response.headers.get("Content-Type"),
        "content_length": len(content)
    }
