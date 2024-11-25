import sys
import time
import os
import requests

# Fungsi untuk mencetak dengan kecepatan khusus
def slow(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

def med(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)

def fast(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 170)

# Fungsi untuk membersihkan layar
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi menampilkan banner
def banner():
    print("""
 ____             _    _            _____           _     
|  _ \  ___  _ __| | _(_)_ __   __ |_   _|__   ___ | |___ 
| | | |/ _ \| '__| |/ / | '_ \ / _` || |/ _ \ / _ \| / __|
| |_| | (_) | |  |   <| | | | | (_| || | (_) | (_) | \__ \\
|____/ \___/|_|  |_|\_\_|_| |_|\__, ||_|\___/ \___/|_|___/
                               |___/    
    """)

# Fungsi memeriksa halaman wp-login.php
def check_wp_login(domain):
    for protocol in ["http://", "https://"]:
        url = f"{protocol}{domain}/wp-login.php"
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            if response.status_code == 200 and "wp-login" in response.text:
                return url
        except requests.exceptions.RequestException:
            continue
    return None

# Fungsi utama
def main():
    if len(sys.argv) != 2:
        slow("Penggunaan: python dork_to_domain.py <dorklist.txt>")
        sys.exit(1)

    # Baca daftar dork dari file
    with open(sys.argv[1], 'r') as file:
        dorks = file.read().splitlines()

    seen_domains = set()  # Hindari duplikasi

    slow("[!] Memulai pengecekan...")
    time.sleep(1)
    clear()
    banner()

    for dork in dorks:
        # Gunakan regex untuk mengambil domain dari dork
        domain = dork.strip().split('/')[0]  # Sederhana, ekstraksi dasar
        if domain not in seen_domains and "." in domain:
            seen_domains.add(domain)
            wp_url = check_wp_login(domain)
            if wp_url:
                print(f"\033[92m{wp_url} > WordPress ditemukan\033[0m")
            else:
                print(f"{domain} > Bukan WordPress atau tidak aktif")

    slow("[!] Proses selesai.")

# Jalankan fungsi utama
if __name__ == "__main__":
    main()
