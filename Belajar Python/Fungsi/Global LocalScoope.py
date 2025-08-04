# Global dan local Scoope

# akses varibel global
nama_global = "Kanya" # Ini adalah variable Global , dimana kita bisa akses di dalam fungsi

def fungsi1():
    print(f"Fungsi menampilkan : {nama_global}")
    
fungsi1()

# akses variabel global dalam loop
for nama in range(0,5):
    print(f" Loop {nama} - {nama_global}")
    
# Akses variabel global dalam percabangan 
if True:
    print(f"if menampilkan : {nama_global}")
    
## Variable local scope
# Tidak bisa mengakses namalokal dari luar hanya berfungsi di dalam fungsi2

def fungsi2():
    nama_lokal = "koyen" # <- variable local scope
    
fungsi2()

## Contoh 1: Penggunaan
def say_oyen():
    print(f"Hello {nama}")
    
nama = "oyen"
say_oyen()

## Contoh 2 : Merubah variable local menjadi global
angka = 0 
nama = "kanya"

def ubah(angkabaru,namabaru):
    global angka # fungsin ini mendapat akses merubah variabel lokal menjadi global 
    global nama
    angka = angkabaru
    nama = namabaru
    
print(f"Sebelum {angka,nama}")
ubah(100,"anya")
print(f"Sesudah {angka,nama}")

## Contoh 3 
# kita bisa mengakses dan merubah variable global dan bisa mengakses local variable untuk (for) dan (if)
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0
    
print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 5
    
print(angka)
print(angka_dummy)
    
