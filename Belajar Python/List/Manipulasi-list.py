# Belajar menggunakan Operasi/Method/Manipulasi list

# Index  0(-3)   1(-2)    2(-1)
data = ["akso","revtuy","asparagus"]

# Mengambil Data Dari List ini
data_0 = data[0]
print(f"Data Index ke-0 : {data_0}")

data_tengah = data[1]
print(f"Data Di Tengah Adalah : {data_tengah}")

data_terakhir = data[-1]
print(f"Data Terakhir Adalah : {data_terakhir}")

# Mengambil info Jumlah Data Yang Ada

panjang_data = len(data)
print(f"Panjang datanya : {panjang_data}")

# Menambahkan item pada list sesuai posisi , Menggunakan (insert)
print(f"Data sebelum ditambah  : \n{data}")

# data.insert(posisi,item)
data.insert(3,"anya") # insert
print(f"ini data setelah ditambahkan : \n{data}")

# Menambah di akhir list , Menggunakan (append)
data.append("risol mayo") # append
print(f"Ini data yang ditambah : \n{data}")

# Menambah List dengan List , Dengan Menggunakan (extend)
data_baru = ["anya","risol mayo","oyen"] # Menggunakan (extend)
data.extend(data_baru) # Menggunakan (extend)
print(f" Data Gabungan : \n{data}")

# Merubah data
# Mengubah data 0 menjadi mewing
data[0] = "mewing"
print(f"Data rubah : \n{data}")

# Remove data / Menghapus data
data.remove("revtuy")# Menggunakan Remove
print(f" Menghapus data : \n{data} ") # Menggunakan Remove
# data.remove("Mewing") # akan error karena huruf haru sesuai yang ada di data "mewing"

# Meremove Data Yang Paling Akhir
data.pop()# Menggunakan pop
print(f"Data Terakhir : \n{data}") # Menggunakan pop

# contoh ke-2
data_terakhir = data.pop()# Menggunakan pop
print(f"Data Terakhir : \n{data}") # Menggunakan pop

print(f"Data terakhir yang dihapus : \n{data_terakhir}")





