import requests

COMMON_PATHS = [
    "/admin", "/administrator", "/adminpanel", "/cpanel", "/login", "/backend",
    "/admin.php", "/admin.html", "/admin/index.php", "/admin/dashboard.php",
    "/admin/login.php", "/admin/controlpanel.php", "/admin/admin.php",
    "/admin/panel.php", "/admin/home.php", "/admin/console.php",
    "/admin/dashboard.html", "/admin/index.html", "/admin/login.html",
    "/admin/controlpanel.html", "/admin/admin.html", "/admin/panel.html",
    "/admin/home.html", "/admin/console.html", "/admin/cp.php",
    "/admin/cp.html", "/admin/manager.php", "/admin/manager.html"
]

def find_admin_panels(base_url):
    found = []
    for path in COMMON_PATHS:
        url = base_url.rstrip("/") + path
        try:
            resp = requests.get(url, timeout=5)
            if resp.status_code == 200:
                found.append(url)
        except requests.RequestException as e:
            print(f"Error occurred while checking {url}: {e}")
            continue
    return found

# Example usage
if __name__ == "__main__":
    base_url = input("Enter the base URL of the website to check: ")
    found_panels = find_admin_panels(base_url)
    if found_panels:
        print("Found admin panels:")
        for panel in found_panels:
            print(panel)
    else:
        print("No admin panels found.")
