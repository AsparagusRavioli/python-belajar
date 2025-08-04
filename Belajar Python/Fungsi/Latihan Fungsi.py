# # Latihan fungsi
import os
# # Program menghitung luas dan keliling persegi panjang
# # Membuat header program
# os.system("cls")

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'='*40:^40}")

# # Mengambil input user
# lebar = int(input("Masukan nilai lebar :"))
# panjang = int(input("Masukan nilai panjang :"))

# # Program menghitung luas
# luas = panjang*lebar
# keliling = 2*(panjang+lebar)

# # Tampilkan hasilnya
# print(f"Hasil  perhitungan Luas : {luas}")
# print(f"Hasil perhitungan Keliling : {keliling}")

# Header
def header():
    '''Fungsi header'''
    os.system("cls")

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'='*40:^40}")
 
# Mengambil input user
def input_user():
    '''Fungsi input user'''
    lebar = int(input("Masukan nilai lebar :"))
    panjang = int(input("Masukan nilai panjang :"))
    
    return lebar,panjang

def hitung_luas(lebar,panjang):
    # Program menghitung luas
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    # Program menghitung keliling
    return 2*(lebar+panjang)
 
def display(message,value):
    print(f"Hasil perhitungan {message} = {value}")

# Program utama   
while True:
    header()
    lebar,panjang = input_user()
    luas = hitung_luas(lebar,panjang)
    keliling = hitung_keliling(lebar,panjang)
    
    display("Luas",luas)
    display("Keliling",keliling)
    
    iscontinue = input("Apakah ingin lanjut (y/n)")
    if iscontinue == "n":
        break
    
print("Akhir dari Program , Terima gaji")
    