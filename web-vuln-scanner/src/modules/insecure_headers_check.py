# src/modules/insecure_headers_check.py

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

SECURITY_HEADERS = [
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "Referrer-Policy"
]

def check_insecure_headers(url):
    missing = []
    try:
        resp = requests.get(url, headers=HEADERS, timeout=5)
        for header in SECURITY_HEADERS:
            if header not in resp.headers:
                missing.append(header)
    except Exception:
        return None
    return missing
