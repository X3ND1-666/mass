import itertools

# Daftar pola username umum cPanel
usernames = [
    "admin", "root", "cpanel", "user", "webmaster", "hosting", "support", "test", 
    "sysadmin", "administrator", "siteadmin", "server", "manager", "operator"
]

# Variasi tambahan dengan domain
domains = ["example", "demo", "test", "mydomain"]
username_variants = [f"{u}{d}" for u in usernames for d in ["", "123", "2024", "admin", "_admin", "_test", "administrator"]]
username_variants += [f"{d}admin" for d in domains]

# Daftar password umum cPanel
passwords = [
    "admin123", "password123", "cpanel2024", "hosting123", "support2024", 
    "root123", "user2024", "pass123", "12345678", "qwerty2024"
]

# Tambahkan variasi simbol dan angka
extra_chars = ['!', '@', '#', '$', '2024']
password_variants = passwords.copy()
password_variants += [pwd + char for pwd in passwords for char in extra_chars]

# Gabungkan semua kombinasi username dan password
combinations = list(itertools.product(username_variants, password_variants))
combinations = [f"{u}|{p}" for u, p in combinations]

# Simpan ke file atau cetak hasilnya
with open('ressult.txt', 'w') as f:
    f.write("\n".join(combinations[:500]))  # Simpan 500 kombinasi pertama

print(f"Total kombinasi: {len(combinations)} (menyimpan 500 kombinasi)")
