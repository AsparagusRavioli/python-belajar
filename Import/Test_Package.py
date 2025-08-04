import sains.matematika
from sains import fisika # Bisa juga menggunakan ini
from sains.fisika import gaya as force # Bisa juga menggunakan ini

hasil_tambah = sains.matematika.tambah(1,2,3,4,5,6)
print(f"Hasil tambah dari package adalah : {hasil_tambah}")

gaya = fisika.gaya(90,10)
print(f"Gaya adalah : {gaya}")

gaya = force(90,10)
print(f"Gaya adalah : {gaya}")

# hasil_perkalian = sains.matematika.perkalian(5,5)
# print(f"Hasil perkalian dari package adalah : {hasil_perkalian}")

# pangkat1 =  sains.matematika.pangkat(5)
# print(f"Hasil pangkat dari package adalah : {pangkat1(3)}")
