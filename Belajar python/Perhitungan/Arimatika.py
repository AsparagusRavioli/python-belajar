a = 11
b = 5

# Operasi Tambah +
hasil = a + b
print(a,'+',b ,'=', hasil)

# Operasi Pengurangan -
hasil = a - b
print(a,'-',b ,'=', hasil)

# Operasi Perkalian *
hasil = a * b
print(a,'*',b ,'=', hasil)

# Operasi Pembagian /
hasil = a / b
print(a,'/',b ,'=', hasil)

# Operasi Eksponen (Pangkat) **
hasil = a ** b
print(a,'**',b ,'=', hasil)

# Operasi Modulus %
hasil = a % b
print(a,'%',b ,'=', hasil)

# Operasi Floor Division 
hasil = a // b
print(a,'//',b ,'=', hasil)


while True:
    user = input("apa kamu mau main gamenya (y/n) :")

    if user == 'n':
        break
    elif user == 'y':
        print("Insert coinnya ")
    else: 
        print("yang bener brok :")