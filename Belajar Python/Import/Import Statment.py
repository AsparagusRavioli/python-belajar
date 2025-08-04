# Import Statment

# Fungsinya adalah untuk mengambil 
# program dari file  external.py

# 1. untuk menyambung program dari eksternal dan menjalankanya
# Hanya print , tanpa data di dalamnya
import tes_import
import Program_oyen

# 2. Import dengan data
import variable
import Import.Program_komeng as Program_komeng

# Data nama di namespace variable 
print(variable.data)
print(Program_komeng.data)

# 3. Import dengan fungsi 
import matematika

hasil = matematika.tambah(5,10)
print(f"Hasil tambah : {hasil}")