# Operasi dan Manipulasi Sebuah String

# 1.Menyambung String (concatenate)
nama_pertama = "akso"
nama_Tengah = "d"
nama_akhir = "sobak"

# ("") --> digunakan untuk membuat space diantara string
nama_lengkap = nama_pertama + " " + nama_Tengah +"'"+ nama_akhir
print(nama_lengkap)

# 2.Menghitung Panjang dari String length (len),untuk menghitung string,
# spasi dan command lainya dihitung
panjang = len(nama_lengkap)
print(" panjang dari "+ nama_lengkap + "=" + str(panjang))

# Operator untuk String
 
# mengecek apakah ada komponen char atau string di string (in)
d = "d"
status = d in nama_lengkap
print( d + "ada di" + nama_lengkap + "=" + str(status))

D = "D"
status = D in nama_lengkap
print( D + "ada di" + nama_lengkap + "=" + str(status))

# Mengecek apakkah dialam komponen tidak terdapat char/string yang dicari (not in)
D = "D"
status = D not in nama_lengkap
print( D + " tidak ada di" + nama_lengkap + "=" + str(status))

d = "d"
status = d not in nama_lengkap
print( d + " tidak ada di" + nama_lengkap + "=" + str(status))

# Pengulangan String loop
print("wkwk"*10)
print(15*"wkwk")

# Indexing untuk mengambil/mempotong  nilai string tertentu ([])
print("index ke-0 adalah :" + nama_lengkap[0])
print("index ke-5 adalah :" + nama_lengkap[5])
# Dimulai dari nilai paling akhir / kanan [-]
print("index ke-[-1] adalah :" + nama_lengkap[-1])
print("index ke-[-3] adalah :" + nama_lengkap[-3])
# Bisa mengambil/potong nilai dengan beberapa bagian yang diinginkan [0:5] ([:])
print("index ke-[0:4] adalah :" + nama_lengkap[0:4])
print("index ke-[3:7] adalah :" + nama_lengkap[3:8])
# Bisa mengambil/memotong nilai secara banyak [::] nilai : diakhir sebagai pembagi setiap nilai yang diambil
print("index ke-[0,2,4,6,8,10,12] adalah :" + nama_lengkap[0:12:2])

# Item paling kecil (min) cara mencarinya dari hitungan alphabet
# untuk melihat nilai string yang paling kecil
print(" Nilai paling kecil = " + min(nama_lengkap))
# Item paling Besar (max) cara mencarinya dari hitungan alphabet
# untuk melihat nilai string yang paling Besar
print(" Nilai paling Besar = " + max(nama_lengkap))


# untuk  mencari senuah ascii_code
ascii_code = ord(" ")
print("ASCII code untuk sebuah spasi adalah :" + str(ascii_code))

ascii_code = ord("=")
print("ASCII code untuk sebuah spasi adalah :" + str(ascii_code))

character = 117
print(" character ASCII code untuk nomor 117 adalah :" + chr(character))


# 4. Operator dalam bentuk method

data = "otong surotong pararotong tong"
jumlah = data.count("o")
print("Jumlah o pada data adalah =",data,"=",str(jumlah))

data = "otong surotong pararotong tong"
jumlah = data.count("o")
print("Jumlah o pada data adalah = " + data + " = " + str(jumlah))

