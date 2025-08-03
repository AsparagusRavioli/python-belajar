import datetime as dt 

print(5*"=","Data diri akso",5*"=")

hari_ini = dt.date.today()
print(f"Hari ini adalah {hari_ini}")
A = f"""
Nama : Akso
Umur : 17
Kelas : 3 SD
Hoby : mancing (mainin alat kencing)    
"""
print(A)


print(f"Masukan tanggal lahir anda bulan,tahun dan hari")
tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan \t: "))
tahun = int(input("Tahun \t: "))



tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tangggal lahir anda adalah : {tanggal_lahir}")

lahir_anda = dt.date.today()
umur_hari = lahir_anda - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f"Umur hari anda adalah : {umur_hari.days} hari")
print(f"Umur Tahun anda adalah : {umur_tahun} Tahun")

print(f"Data diri anda :  \n{A} \nUmur hari : {umur_hari.days} hari  \nUmur \t: {umur_tahun} Tahun")