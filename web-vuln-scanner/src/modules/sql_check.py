# src/modules/sql_check.py

import requests

def check_sqli(url):
    test_payload = "' OR '1'='1"
    # Try injecting into a parameter
    if "?" in url:
        test_url = url + "&id=" + test_payload
    else:
        test_url = url + "?id=" + test_payload
    try:
        resp = requests.get(test_url, timeout=5)
        errors = [
            "You have an error in your SQL syntax",
            "Warning: mysql_",
            "Unclosed quotation mark after the character string",
            "quoted string not properly terminated"
        ]
        for error in errors:
            if error in resp.text:
                return True
    except Exception:
        pass
    return False
