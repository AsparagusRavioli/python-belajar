# Belajar Latihan Perulangan membuat segitiga

sisi = 10

# 1. Menggunakan for 
# Dummy Variable
print("Awal dari for")
print(10*"=","Menggunakan for",10*"=")
count = 1

for i in range(sisi):
    print("*"*count)
    count += 1

print("Akhir dari for")

# 2. Menggunkan While
print(10*"=","Menggunakan While",10*"=")
print("Awal while")

count = 1
while True:
    print("*"*count)
    count += 1
    
    if count > sisi :
        break
    
print("Akhir dari while")

# 3.Hanya menggunakan while saja
print(10*"=","Menggunakan While",10*"=")
print("Awal while")

count = 1
while True:
    if count%2:
        # Print jika Angka Ganjil
        print("*"*count)
        count += 1
        
    else:
        # Akan kembali ke atas jika Ganjil
        count += 1
        continue
    
    # akan break jika count melebihi nilai sisi
    if count > sisi :
        break
    
print("Akhir dari while")

    
# 3.Mmembuat segitiga dengan while
print(10*"=","Menggunakan While",10*"=")
print("Awal while")

count = 1
spasi = int(sisi/2)

while True:
    if count%2:
        # Print jika Angka Ganjil , hanya bisa berlaku (spasi) dengan angka ganjil
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
        
    else:
        # Akan kembali ke atas jika Ganjil
        count += 1
        continue
    
    # akan break jika count melebihi nilai sisi
    if count > sisi :
        break
    
print("Akhir dari while")