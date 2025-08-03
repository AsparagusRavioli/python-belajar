# OPERATOR DALAM BENTUK METHODS!!!

# Merubah case  dari string

# Merubah semua ke upper case (upper)
salam = "bro apa kaps"
print(" ini Normal = " + salam)
salam = salam.upper()
print(" ini UPPER = " + salam)

# Menggunakan methods Capitalize
salam = salam.capitalize()
print(" Ini Capitalize = " + salam)

# Menggunakan methods swapcase
tes_swapcase = "Ayam Goreng Suharti"
cek_hasil = tes_swapcase.swapcase()
print(cek_hasil)

# 2) casefold() <-- sama dengan lower()
# bedanya, casefold() mengkonversi karakter tidak umum menjadi lowercase karakter umum
# Contoh  : 'ß' (german) = menjadi 'ss'

tes_casefold = "außen IS AN GERMAN WORD"
cek_hasil = tes_casefold.casefold()
print(cek_hasil)

# 4 expandtabs () <-- Mengatur lebar tab (\t)
tes_expandtabs = "Ayam\tGoreng\tSuharti"
cek_hasil = tes_expandtabs.expandtabs(10)
print(cek_hasil)

# Merubah semua ke lower case (lower)
alay = "aku keycCe abisZSZSZSZSZS"
print(" ini normal = " + alay)
alay = alay.lower()
print(" ini lower = " + alay)

## Pengecekan dengan method ISX methods

# contoh pengecekan lower case dan Upper case
salam = "sist"
apakah_lower = salam.islower() # hasil nya boolean
print(salam + " is lower = " + str(apakah_lower))

salam = "SIST"
apakah_upper = salam.isupper() # hasil nya boolean
print(salam + " is lower = " + str(apakah_upper))

salam = "sist"
apakah_upper = salam.isupper() # hasil nya boolean
print(salam + " is lower = " + str(apakah_upper))


# isalpha() <--- untuk mengecek semuanya huruf
# isalnum() <--- untuk mengecek semua huruf dan angka
# isdecimal() <-- untuk mengecek angka saja
# isspace() <--- untuk spas,tab,newline \n
# istitle() <--- semua kata dimulai dengan huruf besar

# isalpha() <--- untuk mengecek semuanya huruf
hurup = "ini adalah hurup yagesya"
cek_hurup = hurup.isalpha()
print(hurup + " is alpha = " + str(cek_hurup))

# isalnum() <--- untuk mengecek semua huruf dan angka
hurupandangka = "ini adalah 10 dan hurup 10 10 10 "
cek_hurupangka = hurupandangka.isalnum()
print(hurupandangka + " is alnum = " + str(cek_hurupangka))

# istitle() <--- semua kata dimulai dengan huruf besar
judul = "It Is Okay To Not Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() <--- keren

# Menggunakan startswith(),yang dibaca yang di depan --> contoh ("(/Sangjanim/) oppa ")
cek_start = "Sangjangnim oppa".startswith("Sangjangnim") # --> jadi  yang didalam  harus sama persis --> jika tidak akan menjadi false ""
print("start =" + str(cek_start))

cek_start = "Sangjangnim oppa".startswith("sangjangnim") # --> jadi  yang didalam  harus sama persis --> jika tidak akan menjadi false ""
print("start =" + str(cek_start))

# Menggunakan endswith(),yang dibaca yang di belakang --> contoh ("Sangjanim (/Oppak/) ")
cek_end = "Sangjanim Oppak".endswith("Oppak") # --> jadi  yang didalam  harus sama persis --> jika tidak akan menjadi false ""
print("start =" + str(cek_end))

cek_end = "Sangjanim Oppak".endswith("Oppak") # --> jadi  yang didalam  harus sama persis --> jika tidak akan menjadi false ""
print("start =" + str(cek_end))

##  pengecek penggabungan methods join() split()
# Menggunakan methods Join()
pisah = ['aku','sayang','kamu','ciusss'] #  ['aku','sayang','kamu','ciusss'] ini adalah list
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)


gabungan = ' ehm '.join(pisah)
print(gabungan)

# Menggunakan methods Split()

gabungan = "akuehmsayangehkamu"
print(gabungan.split('ehm'))

## alokasi karakter rjust() ljust() center()

# Menggunakan Methods rjust()
kanan = "kanan".rjust(10,"_")
print("'"+kanan+"'")

kiri = "kiri".ljust(10,"-")
print("'"+kiri+"'")
# Menggunakan Methods ljust()
kiri = "kiri".ljust(10)
print("'"+kiri+"'")

kiri = "kiri".ljust(10,"=")
print("'"+kiri+"'")

# Menggunakan Methods Center()
tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(10,"#")
print("'"+tengah+"'")

# Kebalikanya Strip() untuk menghapus
tengah =tengah.strip("#")
print("'"+tengah+"'")