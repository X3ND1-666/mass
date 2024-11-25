import sys
import requests
from urllib.parse import urlparse

# Fungsi untuk memeriksa apakah halaman wp-login.php ada
def check_wordpress_login(domain):
    for protocol in ["http://", "https://"]:
        url = f"{protocol}{domain}/wp-login.php"
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            if response.status_code == 200 and "wp-login" in response.text:
                return url  # Domain valid WordPress
        except requests.exceptions.RequestException:
            continue  # Coba protokol berikutnya jika gagal
    return None

# Fungsi utama
def main():
    if len(sys.argv) != 2:
        print("Penggunaan: python dork_to_wp_checker.py <listdork.txt>")
        sys.exit(1)

    # Membaca daftar dork dari file
    with open(sys.argv[1], 'r') as file:
        dorks = file.read().splitlines()

    # Periksa setiap domain dan simpan hasil valid
    with open("ress.txt", 'w') as output_file:
        for dork in dorks:
            domain = urlparse(dork).netloc or dork  # Ambil domain dari URL dork
            wp_login_url = check_wordpress_login(domain)
            if wp_login_url:
                print(f"{wp_login_url} > WordPress ditemukan")
                output_file.write(wp_login_url + "\n")  # Tulis domain valid ke file
            else:
                print(f"{domain} > Bukan WordPress atau tidak aktif")

if __name__ == "__main__":
    main()
