# Belajar string and width

data_nama = "amin"
data_umur = "77"
data_tinggi = "177.5"
data_tinggal = "Ciputat"
data_sepatu = "41"
data_hoby = "rpeh"


# String
data_string = f"Nama = {data_nama}, \nUmur = {data_umur}, \nTinggal = {data_tinggal}, \nSepatu = {data_sepatu}, \nHoby = , {data_hoby}, \nTinggi Badan {data_tinggi}"
print(7*"=","Data String",7*"=")
print(data_string)

# String Multiline (Kutip Triplets (""""""))
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
"""

print(7*"=","Data String Multiline",7*"=")
print(data_string)

# Mengatur Lebar (:>(bisa menggunakan nomor berapa saja))
data_nama = "Amin"
data_string = f"""
nama = {data_nama:}
nama = {data_nama:>10}
umur = {data_umur:>3}
tinggi = {data_tinggi:>4}
"""

print(7*"=","Mengatur Lebar",7*"=")
print(data_string)

