# PROGRAM : DICTIONARY
mahasiswa = {
    "nama": "Dermawan",
    "nim": "D0425319",
    "jurusan": "Sistem Informasi"
}

# Mengakses nilai
print("nama:", mahasiswa["nama"])

# Menambah data baru
mahasiswa["angkatan"] = 2025

# Mengubah data
mahasiswa["jurusan"] = "Sistem informasi"

# Menghapus data
del mahasiswa["nim"]

# Menampilkan seluruh isi dictionary
print("data mahasiswa:", mahasiswa)
