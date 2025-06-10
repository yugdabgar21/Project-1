import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

SECURITY_HEADERS = [
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "Referrer-Policy",
    "X-XSS-Protection",  # Deprecated but still worth checking
    "Expect-CT",         # Expect-CT (Certificate Transparency)
    "Feature-Policy",    # Feature Policy
    "Permissions-Policy" # Permissions Policy (replaces Feature-Policy)
]

def check_insecure_headers(url):
    missing = []
    recommendations = {
        "X-Frame-Options": "Set to 'DENY' or 'SAMEORIGIN' to prevent clickjacking attacks.",
        "X-Content-Type-Options": "Set to 'nosniff' to prevent MIME type sniffing.",
        "Strict-Transport-Security": "Set to 'max-age=31536000; includeSubDomains' to enforce HTTPS.",
        "Content-Security-Policy": "Set to a strict policy to prevent XSS and other injection attacks.",
        "Referrer-Policy": "Set to 'strict-origin-when-cross-origin' to control referrer headers.",
        "X-XSS-Protection": "Set to '1; mode=block' to enable XSS filtering (deprecated but still useful).",
        "Expect-CT": "Set to 'max-age=31536000' to enforce Certificate Transparency.",
        "Feature-Policy": "Set to a strict policy to control which features the browser should use.",
        "Permissions-Policy": "Set to a strict policy to control which features the browser should use."
    }
    try:
        resp = requests.get(url, headers=HEADERS, timeout=5)
        for header in SECURITY_HEADERS:
            if header not in resp.headers:
                missing.append(header)
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
    return missing, recommendations

# Example usage
if __name__ == "__main__":
    test_url = "http://example.com"
    result = check_insecure_headers(test_url)
    if result:
        missing_headers, recommendations = result
        if missing_headers:
            print("Missing security headers:")
            for header in missing_headers:
                print(f"- {header}: {recommendations[header]}")
        else:
            print("All recommended security headers are present.")
    else:
        print("Failed to retrieve headers.")
