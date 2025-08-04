import datetime
import os
import string
import random

# Template dict Mahasiswa
mahasiswa_template = {
    'nama': '',
    'nim': '',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111,1,1)
}

data_mahasiswa = {}

while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*22)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Masukan Nama Anda : ")
    mahasiswa['nim'] = input("Masukan Nim Anda : ")
    mahasiswa['sks_lulus'] = int(input("Masukan SKS Anda : "))
    
    tahun_lahir = int(input("Tahun lahir anda (YYYY) : "))
    bulan_lahir = int(input("Bulan lahir anda (1-12) : "))
    tanggal_lahir = int(input("Tanggal lahir anda (1-31) : "))
    mahasiswa['lahir'] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)

    KEY = " ".join(random.choice(string.ascii_uppercase)for i in range (6))
    data_mahasiswa.update({KEY:mahasiswa})

    # Tampilkan semua data
    print(F"\n{'KEY':<10} {'NAMA':<13} {'NIM':<10} {'SKS Lulus':<11} {'LAHIR':<13}")
    print("-"*60)

    for key in data_mahasiswa:
        nama = data_mahasiswa[key]['nama']
        nim = data_mahasiswa[key]['nim']
        sks = data_mahasiswa[key]['sks_lulus']
        lahir = data_mahasiswa[key]['lahir'].strftime("%x")

        print(F"{key:<10} {nama:<13} {nim:<10} {sks:<11} {lahir:<13}")

    print("\n")
    is_done = input("Apa sudah selesai bro? (y/n): ")
    if is_done.lower() == "n":
        break

print("\n Akhir dari program")