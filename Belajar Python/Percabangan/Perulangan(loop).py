# Belajar Program Menggunakan Perulangan/LOOP

# Perulangan LOOP (for in)

# for kondisi:
# aksi

angka2_list = [0,1,2,3,4,5,6,7,8,9,10] # ini adalah list 
print(angka2_list)

for i in angka2_list:
    print(f"Nilai i sekarang --> {i}")
    
print("\nAkhir dari porgram 1 \n")

# ini dengan Range , menggunakan methods Range() , Range digunakan untuk mengambi nilai yang diingikan
angka2_range = range(5)

for i in angka2_range:
    print(f"Nilai i sekarang --> {i}")

print("\nAkhir dari porgram 2 \n")
    
angka2_range = range(1,5)

for i in angka2_range:
    print(f"Nilai i sekarang --> {i}")

print("\nAkhir dari porgram 3 \n")

# Menggunakan String

data = "Saya tamvan syekali"

for huruf in data:
    print(huruf)