import json
import os

def load_json_file(filename):
    """Muat file JSON dengan aman."""
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' tidak ditemukan.")
        return None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"❌ File '{filename}' tidak valid atau rusak.")
        return None

# Muat data dari file JSON
followers_data = load_json_file('followers_1.json')
following_data = load_json_file('following.json')

# Jika ada file yang tidak bisa dimuat, hentikan program
if followers_data is None or following_data is None:
    print("⛔ Program dihentikan karena file JSON tidak valid.")
    exit()

# Ambil username dari followers
followers_usernames = {
    item['string_list_data'][0]['value']
    for item in followers_data
    if 'string_list_data' in item and item['string_list_data']
}

# Ambil username dari yang kamu follow
following_usernames = {
    item['string_list_data'][0]['value']
    for item in following_data.get('relationships_following', [])
    if 'string_list_data' in item and item['string_list_data']
}

# Hitung perbandingan
not_following_back = following_usernames - followers_usernames
not_followed_back = followers_usernames - following_usernames

# Cetak hasil
print("\n📌 Yang kamu follow tapi tidak follback:")
if not not_following_back:
    print("✅ Semua orang yang kamu follow sudah follback.")
else:
    for username in sorted(not_following_back):
        print("-", username)

print("\n📌 Yang follow kamu tapi tidak kamu follback:")
if not not_followed_back:
    print("✅ Kamu sudah follback semua followers-mu.")
else:
    for username in sorted(not_followed_back):
        print("-", username)