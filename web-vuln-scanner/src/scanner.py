# src/scanner.py

import sys
import os
from colorama import Fore, Style, init

sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

from admin_panel_check import find_admin_panels
from xss_check import check_xss
from sql_check import check_sqli
from insecure_headers_check import check_insecure_headers

init(autoreset=True)

def banner():
    print(Fore.CYAN + r"""
 __        __   _      __     __     _         ____                                  
 \ \      / /__| |__   \ \   / /   _| |_ __   / ___|  ___ __ _ _ __  _ __   ___ _ __ 
  \ \ /\ / / _ \ '_ \   \ \ / / | | | | '_ \  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
   \ V  V /  __/ |_) |   \ V /| |_| | | | | |  ___) | (_| (_| | | | | | | |  __/ |   
    \_/\_/ \___|_.__/     \_/  \__,_|_|_| |_| |____/ \___\__,_|_| |_|_| |_|\___|_|   
  _             __  __    _    ____ _____ _____ ____        ____                     
 | |__  _   _  |  \/  |  / \  / ___|_   _| ____|  _ \ __  _|  _ \                    
 | '_ \| | | | | |\/| | / _ \ \___ \ | | |  _| | |_) |\ \/ / | | |                   
 | |_) | |_| | | |  | |/ ___ \ ___) || | | |___|  _ <  >  <| |_| |                   
 |_.__/ \__, | |_|  |_/_/   \_\____/ |_| |_____|_| \_\/_/\_\____/                    
        |___/                                                                        
""")
    print(Fore.YELLOW + "Web Vulnerability Scanner\n")

def main():
    banner()
    target = input(Fore.GREEN + "Enter target URL (e.g., https://example.com): ").strip()
    print(Fore.BLUE + "\n[+] Scanning for exposed admin panels...")
    panels = find_admin_panels(target)
    if panels:
        print(Fore.RED + "[!] Exposed admin panels found:")
        for panel in panels:
            print(Fore.RED + " -", panel)
    else:
        print(Fore.GREEN + "[+] No common admin panels found.")

    print(Fore.BLUE + "\n[+] Checking for SQL Injection vulnerabilities...")
    sql_vuln = check_sqli(target)
    if sql_vuln:
        print(Fore.RED + "[!] SQL Injection vulnerability detected!")
    else:
        print(Fore.GREEN + "[+] No SQL Injection vulnerability detected.")

    print(Fore.BLUE + "\n[+] Checking for XSS vulnerabilities...")
    xss_vuln = check_xss(target)
    if xss_vuln:
        print(Fore.RED + "[!] XSS vulnerability detected!")
    else:
        print(Fore.GREEN + "[+] No XSS vulnerability detected.")

    print(Fore.BLUE + "\n[+] Checking for insecure HTTP headers...")
    missing_headers = check_insecure_headers(target)
    if missing_headers is None:
        print(Fore.YELLOW + "[!] Could not retrieve headers (connection issue).")
    elif missing_headers:
        print(Fore.RED + "[!] Missing security headers:")
        for h in missing_headers:
            print(Fore.RED + " -", h)
    else:
        print(Fore.GREEN + "[+] All important security headers are present.")

if __name__ == "__main__":
    main()
