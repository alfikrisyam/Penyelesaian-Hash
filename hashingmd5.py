import hashlib

# Daftar absen kelas IF III C
daftar_absen = [
    {"NIM": "10223003", "Nama": "MAULANA ADITYA"},
    {"NIM": "10223004", "Nama": "ZENAL ARIPIN"},
    {"NIM": "10223016", "Nama": "NUR FAIZAH"},
    {"NIM": "10223017", "Nama": "EKA MAULIDA"},
    {"NIM": "10223023", "Nama": "ENCENG YUSRIL HIDAYATULLOH"},
    {"NIM": "10223029", "Nama": "ANGGI MAYUSRI"},
    {"NIM": "10223030", "Nama": "ABDUH ZAHID ATTHOLIBI"},
    {"NIM": "10223032", "Nama": "ARY FIRMANSYAH"},
    {"NIM": "10223038", "Nama": "LENI NURUL ISTIQOMAH"},
    {"NIM": "10223039", "Nama": "REYHAN EKKY KUSUMA R"},
    {"NIM": "10223048", "Nama": "MOHAMMAD BISRI MUSTHAFA"},
    {"NIM": "10223050", "Nama": "MUHAMMAD RAIHAN ABDUH"},
    {"NIM": "10223056", "Nama": "RIFAL HIKMATUL AKMAL"},
    {"NIM": "10223058", "Nama": "DELA DELIANSYAH"},
    {"NIM": "10223059", "Nama": "SEPTIAN MAULANA BARKAH"},
    {"NIM": "10223064", "Nama": "NAZWA SITI FAUZIAH"},
    {"NIM": "10223069", "Nama": "RENDI FAUZI"},
    {"NIM": "10223072", "Nama": "AL FIKRI SYAM ABDUL HANIF"},
    {"NIM": "10223076", "Nama": "WINDA NOOR DINI"},
    {"NIM": "10223078", "Nama": "ZULFA STANIA"},
    {"NIM": "10223079", "Nama": "NABIL ABDUL BASIT"},
    {"NIM": "10223105", "Nama": "DANI ALPU DAROJAT"},
    {"NIM": "10223110", "Nama": "AGI ABDUL GANI"},
    {"NIM": "10223112", "Nama": "AGNIA AMALIA"},
    {"NIM": "10223116", "Nama": "MUHAMAD NAJIB RAMDAN"},
    {"NIM": "10223120", "Nama": "RIYAD MUHAMMAD ROBANI"}
]

# Fungsi untuk menghasilkan hash MD5
def generate_md5_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

# Menghasilkan hash untuk setiap mahasiswa
hasil_hash = []
for mhs in daftar_absen:
    gabungan = mhs["NIM"] + mhs["Nama"]
    hash_value = generate_md5_hash(gabungan)
    hasil_hash.append({"NIM": mhs["NIM"], "Nama": mhs["Nama"], "Hash": hash_value})

# Menampilkan hasil
for hasil in hasil_hash:
    print(f"NIM: {hasil['NIM']}, Nama: {hasil['Nama']}, Hash: {hasil['Hash']}")