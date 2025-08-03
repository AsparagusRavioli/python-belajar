# Fungsi dengan return / return value kembalian

# template fungsi dengan kembalian
# def nama_fungsi(argument):
#      badan fungsi
#      return output


# Fungsi kuadrat

def kuadrat(angka):
    '''Fungsi kuadrat'''
    output_kuadrat = angka**2
    return output_kuadrat

y = kuadrat(7)
print(y)

print(kuadrat(10))

z = 100 + kuadrat(3)
print(z)

# Fungsi tambah

def fungsi_tambah(angka_1,angka_2):
    '''Fungsi return dengan multi input'''
    return angka_1 + angka_2


a = fungsi_tambah(10,33)
print(a)

# Fungsi dengan return banyak 

def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    return tambah,kurang,kali,bagi
    
k,l,m,n = operasi_matematika(9,5)

print(f"Hasil tambah : {k}")
print(f"Hasil kurang : {l}")
print(f"Hasil perkalian : {m}")
print(f"Hasil pembagian : {n}")