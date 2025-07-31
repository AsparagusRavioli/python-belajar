# Belajar program Break


# Break Digunakan untuk memberhentikan atau mengstop variable true yang sudah ditemukan

# Contoh ke-1
print(10*"=","Contoh ke-1",10*"=")
angka = 0

while angka < 5:
    angka += 1
    print(f"Nilai angka sekarang ---> {angka}")
    
    if angka == 3:
        print("nyoman")
        break
    
    print("yomaann")

print("cyukup yah")

print(10*"=","Contoh ke-2",10*"=")
# Contoh ke-2

data_int = int(input("Masukan Nomor yang ingin dihitung  : "))

angka = 0

while True:
    angka += 1
    print(f"Nilai angka sekarang ---> {angka}")
    
    if angka == data_int:
        print("nyoman")
        break
    
    print("yomaann")

print("cyukup yah")