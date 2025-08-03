# Belajar Operasi list

data_angka = [1,2,3,4,4,5,3,6,8,9,0,10,3,3,4,4,4]

# Menggunakan Count

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f" Jumlah data angka 4 : {jumlah_data_4}")
print(f" Jumlah data angka 3 : {jumlah_data_3}")

# Mengambil Posisi Data (Index)
data = ["kanya","oyen","komeng","risolmayo"]
print(f"Data : {data}")

index_oyen = data.index("oyen") # Mengunakan index
index_komeng = data.index("komeng") # Mengunakan index
print(f"Index si oyen adalah : {index_oyen}")
print(f"Index si komeng adalah : {index_komeng}")

# Mengurutkan Data List Numbers , Meneggunakan (sort)
print(f"ini adalah data sebelum diurutkan/sort : \n{data_angka}")
data_angka.sort() # Diurutkan dari nilai terkecil sampai terbesar
print(f"Ini adalah data angka yang sudah diurutkan/sort : \n{data_angka} ")

# Mengurutkan Data List String , Meneggunakan (sort)
print(f"Data string sebelum di urutkan/sort : \n{data}")
data.sort() # Diurutkan sesuai alphabet 
print(f"Ini data string yang sudah di urutkan/sort : \n{data}")

# Membalik listnya dari yang terbesar ke terkecil , Mengunakan (Reverse)
data_angka.reverse()# dari yang terbesar ke terkecil
data.reverse()# dari yang terbesar ke terkecil
print(f"Data di reverse : \n{data_angka}  \n{data}")