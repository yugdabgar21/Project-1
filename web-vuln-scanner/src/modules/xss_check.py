# src/modules/xss_check.py

import requests

def check_xss(url):
    test_payload = "<script>alert(1)</script>"
    # Try injecting into a parameter
    if "?" in url:
        test_url = url + "&xss=" + test_payload
    else:
        test_url = url + "?xss=" + test_payload
    try:
        resp = requests.get(test_url, timeout=5)
        if test_payload in resp.text:
            return True
    except Exception:
        pass
    return False
