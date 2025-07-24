# Logika komparasi 
#Membuat gabungan area rentang dari rangka 
#++++++++3----------10+++++++


inputuser = float(input ("Masukan angka yang \nbernilai kurang dari 3 atau lebih dari 10 :\n"))

# ++++++3------10++++++
# Memeriksa angka kurang dari 3
iskurangdari = (inputuser < 3)
print("Angka yang kurang dari 3 =1",iskurangdari)

islebihdari = (inputuser > 10)
print("Angka yang lebih dari 10 =",islebihdari)


# ++++++3-------10++++

isCorrect = iskurangdari or islebihdari
print("Masukan angka yang benar",isCorrect)

# --------3++++++10-------
# kasus irisan

inputuser = float(input ("Masukan angka yang \nbernilai LEBIH dari 3 atau kurang dari 10 :\n"))

# ----3+++++++++
iskurangdari = (inputuser > 3)
print("Angka yang lebih dari 3 =",iskurangdari)

# ++++10---------
islebihdari = (inputuser < 10)
print("Angka yang kurang dari 10 =",islebihdari)

isCorrect = iskurangdari and islebihdari
print("Masukan angka yang benar",isCorrect)


InputUser = float(input("Masukkan Angka :"))

print("-----0+++++5-----8+++++11-----") 
# true jika 1 atau 2 atau 3 atau 4 atau 5 atau 9 atau 10

IsLebihDari0 = InputUser > 0
IsKurangDari5 = InputUser < 5 
IsLebihDari8 = InputUser > 8
IsKurangdari11  = InputUser < 11
Cara1Soal1 = IsLebihDari0 and IsKurangDari5 or IsLebihDari8 and IsKurangdari11
print("Status Cara 1: ", Cara1Soal1)


