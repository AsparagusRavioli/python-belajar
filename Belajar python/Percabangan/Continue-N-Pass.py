# Belajar Contniue,Pass,and Break

# Pass -> dia berfungsi sebagai dummy , tidak akan dieksekusi

angka = 0

while angka < 5:
    angka += 1
    print(angka)
    if angka == 3:
       pass # ini tidak akan dieksekusi 
   
# Continue

angka_1 = 0
print(f"Nilai angka sekarang --> {angka_1}")


while angka_1 < 5:
    angka_1 += 1
    print(f"Nilai angka sekarang --> {angka_1}")# Aksi ke satu 1

    if angka_1 == 3:
        print("noice")
        continue # akan membuat loop meloncat ke step selanjutnya , akan melewati aksi ke dua (2)
    
    print("shiball")# Aksi ke dua 2
        
print("pinish ygy")

    