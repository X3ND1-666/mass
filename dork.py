import sys
import requests
import re
from urllib.parse import urlparse

# Fungsi untuk mengekstrak domain dari teks menggunakan regex
def extract_domain(line):
    match = re.search(r'(https?://)?(www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', line)
    if match:
        return match.group(3)  # Ambil hanya domain utama
    return None

# Fungsi untuk memeriksa halaman wp-login.php
def check_wordpress_login(domain):
    for protocol in ["http://", "https://"]:
        url = f"{protocol}{domain}/wp-login.php"
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            if response.status_code == 200 and "wp-login" in response.text:
                return url  # Ditemukan halaman WordPress
        except requests.exceptions.RequestException:
            continue  # Coba dengan protokol berikutnya
    return None

# Fungsi utama untuk membaca daftar dork dan memprosesnya
def main():
    if len(sys.argv) != 2:
        print("Penggunaan: python script.py <listdork.txt>")
        sys.exit(1)

    # Membaca daftar dork dari file
    with open(sys.argv[1], 'r') as file:
        lines = file.read().splitlines()

    # Proses setiap baris, ekstrak domain, dan periksa WordPress
    seen_domains = set()  # Hindari duplikasi domain
    for line in lines:
        domain = extract_domain(line)
        if domain and domain not in seen_domains:
            seen_domains.add(domain)
            wp_login_url = check_wordpress_login(domain)
            if wp_login_url:
                print(f"\033[92m{wp_login_url} > WordPress ditemukan\033[0m")  # Warna hijau
            else:
                print(f"{domain} > Bukan WordPress atau tidak aktif")

if __name__ == "__main__":
    main()
