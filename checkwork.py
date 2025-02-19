# ────────────────────────────────────────────────
#  📌 Developed by Commit420 | https://github.com/Commit420  
#────────────────────────────────────────────────
#  ✅ Open-source & free to use for legal, experimental purposes.  
#  ⚠️ Unauthorized or illegal use is strictly prohibited.  
# ────────────────────────────────────────────────

# Version 1.0.0
# NC24-weblink-bruteforce (checkwork Add-on)

# (!) Dieses Add-on dient zur Überprüfung einer blockierung.

import requests
from colorama import Fore, Style, init

init(autoreset=True)

url = "https://changemebecauseimnotfilehost.host/i/2yU1dHx"

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        print(f"{Fore.GREEN}[+] URL erreichbar: {url}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[-] URL nicht erreichbar: {url} (Status: {response.status_code}){Style.RESET_ALL}")
except requests.RequestException as e:
    print(f"{Fore.RED}[-] Fehler beim Abrufen der URL: {e}{Style.RESET_ALL}")
