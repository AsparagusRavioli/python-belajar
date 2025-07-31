# Belajar Menggunakan Deep Copy Nested List


## Nested list biasa
data_0 = [1,2,3]
data_1 = [4,5,6,7,8]

data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()

print(f"ini data copy  : \n{data_2D_copy}")
print(f"Ini list di dalam list ygy : \n{data_2D}")

# Mengambil Data dari nested list
data = data_2D[0][0]# Step pertama [0] --> masuk ke listnya , Step ke 2 [0] --. Mengaambil posisi list yang ingin di ambil
print(f"data = {data}")
# Contoh ke-2
data = data_2D[1][4]# Step pertama [0] --> masuk ke listnya , Step ke 2 [0] --. Mengaambil posisi list yang ingin di ambil
print(f"data = {data}")

# Addres semuanya

print(f"ini address asli : {hex(id(data_2D))}")
print(f"ini address copy : {hex(id(data_2D_copy))}")

print(f"addres dari member ke-1 :\n")
print(f"ini address asli : {hex(id(data_2D[0]))}")
print(f"ini address copy : {hex(id(data_2D_copy[0]))}")

# yang bisa berubah/bisa di COPY hanyalah yang di luar/BUKAN dari list itu sendiri seperti 10 dan 11 itu diluar dari list
data = data_2D[1][0] = 10
data = data_2D[2] = 11
print(f"ini data copy  : \n{data_2D_copy}")
print(f"Ini list di dalam list ygy : \n{data_2D}")

# Menggunakan Deep Copy

from copy import deepcopy # harus mengimport terlebih dahullu jika ingin digunakan
data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)


print(f"ini address asli : {hex(id(data_2D))}")
print(f"ini address deepcopy : {hex(id(data_2D_deepcopy))}") # addres nya tidak ada perubahan sama sekali

print(f"addres dari member ke-1 :\n")
print(f"ini address asli : {hex(id(data_2D[0]))}")
print(f"ini address deepcopy : {hex(id(data_2D_deepcopy[0]))}")  # Ada perbedaan address di sini

# Menggunakan Deep Copy , from copy import deepcopy , jadi kita harus menggunakan deepcopy agr bisa mengcopy
data = data_2D[1][0] = 100
print(f"data : \n{data_2D}")
print(f"Ini list di dalam list ygy : \n{data_2D}")
print(f"ini data copy  : \n{data_2D_deepcopy}")