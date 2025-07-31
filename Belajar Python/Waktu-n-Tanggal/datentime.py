# Belajar Date and Time

import datetime as dt

hari_ini_today = dt.date.today()

print(hari_ini_today)
print(f"Hari ini adalah = {hari_ini_today:%A}")# Methods (:%A) --> untuk mencari hari apa

tanggal = dt.date(2008,7,2)

print(tanggal)
print(f"Hari ini adalah = {tanggal:%A}")

print(7*"=","Data lahir",7*"=")
print(f"Tolong Masukan tanggal,\ntahun dan bulan lahir anda")
Tanggal = int(input("Tanggal \t:"))
Bulan = int(input("Bulan \t\t:"))
Tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(Tahun,Bulan,Tanggal)
print(f"Tanggal lagi adalah : {tanggal_lahir}")
print(f"Hari ini adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini adalah : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30

print(f"Hari ini adalah : {tanggal_lahir:%A}")
print(f"Umur hari mu adalah : {umur_hari.days}")
print(f"Umur mu adalah \t: {umur_tahun} Tahun , {umur_bulan} Bulan")