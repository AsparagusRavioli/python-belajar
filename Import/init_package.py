import package
from package.matematika import scientific # bisa juga menggunakan ini lebih simple

hasil_tambah = package.matematika.tambah(1,2,3,4,5,6,7,8)
print(f"Hasil tambah : {hasil_tambah}")

hasil_fisika = package.fisika.gaya(11,9)
print(f"Hasil fisika : {hasil_fisika}")

hasil_kali = package.matematika.kali(17,9) 
print(f"Hasil kali : {hasil_kali}")

pangkat_3 = scientific.pangkat(3) 
print(f"Hasil pangkat 3 : {pangkat_3(5)}")

# from package import *

# hasil_tambah = matematika.basic.tambah(1,2,3,4,5,6,7,8)
# print(f"Hasil tambah : {hasil_tambah}")

# hasil_fisika = fisika.gaya(11,9)
# print(f"Hasil fisika : {hasil_fisika}")

# hasil_kali = matematika.basic.kali(17,9) 
# print(f"Hasil kali : {hasil_kali}")
