# src/modules/admin_panel_check.py

import requests

COMMON_PATHS = [
    "/admin", "/administrator", "/adminpanel", "/cpanel", "/login", "/backend"
]

def find_admin_panels(base_url):
    found = []
    for path in COMMON_PATHS:
        url = base_url.rstrip("/") + path
        try:
            resp = requests.get(url, timeout=5)
            if resp.status_code == 200:
                found.append(url)
        except requests.RequestException:
            continue
    return found
