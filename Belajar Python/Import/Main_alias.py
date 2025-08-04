# module matematika dengan import

from matematika1 import tambah as add
from matematika1 import kali 
from matematika1 import pangkat as seterah_kalian_mau_apa
import matematika1 as math # <--- bisa dilakukan

hasil_tambah = add(1,2,3,4,5,6)
print(f"Hasil fungsi tambah : {hasil_tambah}")

hasil_kali = math.kali(1,2,3,4,5)
print(f"Hasil fungsi perkalian : {hasil_kali}")

pangkat_3 = seterah_kalian_mau_apa(3)
print(f"Hasil fungsi perkalian : {pangkat_3(3)}")