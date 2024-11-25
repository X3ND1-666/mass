import sys
import requests
from requests.auth import HTTPBasicAuth

def add_admin(domain, wp_user, wp_pass, new_user, new_pass, new_email):
    try:
        # URL endpoint REST API untuk menambah pengguna
        url = f"http://{domain}/wp-json/wp/v2/users"
        
        # Data pengguna baru
        user_data = {
            "username": new_user,
            "password": new_pass,
            "email": new_email,
            "roles": ["administrator"]
        }

        # Permintaan POST dengan autentikasi dasar
        response = requests.post(url, json=user_data, auth=HTTPBasicAuth(wp_user, wp_pass))

        # Validasi hasil
        if response.status_code == 201:
            print(f"[SUCCESS] Admin user added to {domain}")
        else:
            print(f"[FAILED] Could not add admin to {domain}: {response.text}")
    except Exception as e:
        print(f"[ERROR] {domain} - {str(e)}")

# Fungsi utama
def main():
    if len(sys.argv) != 2:
        print("Penggunaan: python add_admin.py <listdomain.txt>")
        sys.exit(1)

    # Load domain dari file
    with open(sys.argv[1], 'r') as file:
        domains = file.read().splitlines()

    # Input data admin baru
    new_user = "newadmin"
    new_pass = "StrongPassword123!"
    new_email = "newadmin@example.com"

    # Loop setiap domain
    for domain in domains:
        add_admin(domain, "existing_admin", "existing_password", new_user, new_pass, new_email)

if __name__ == "__main__":
    main()
