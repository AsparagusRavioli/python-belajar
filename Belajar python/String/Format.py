# Format String

# Contoh generic

# Menggunakan Sebuah Format (f)
# String
nama = "Akso amin"
format_str = f"Hello {nama}"
print(format_str)

# Boolean
Boolean = True
format_str = f"Boolean = {Boolean}"
print(format_str)

# Angka
angka = "2008.8"
format_str = f"Angka = {angka}"
print(format_str)

# Angka Bilangan bulat {angka:d} :d untuk menampilkan bahwa angka ini adalah bilangan bulat
angka = 15
format_str = f"Bilangan bulat = {angka:d}"
print(format_str)

# Bilangan dengan ordo Ribuan (:,)
angka = 2008
format_str = f"Bilangan Ribuan = {angka:,}"
print(format_str)

# Bilangan dengan ordo jutaan (:,)
angka = 20000000
format_str = f"Bilangan Jutaan = {angka:,}"
print(format_str)

# Bilangan Desimal , (:.) (3) untuk angka desimal yang ingin diambil (f) untuk float
angka = 2008.810210930912301
format_str = f"Angka = {angka:.3f}"
print(format_str)

# Menampilkan Leading Zero , Menambahkan nilai di depan yang kosong
angka = 2008.810210930912301 
format_str = f"Angka = {angka:10.3f}"
print(format_str)

angka = 2008.810210930912301 
format_str = f"Angka = {angka:010.3f}"
print(format_str)

# Menampilkan  Tanda  + dan - , dengan cara menambahkan methods (:+d) di dalam format {}
angka_minus = -10
angka_plus = +10
angka_pluss = +10.12381
format_min = f" Minus = {angka_minus:+d}"
format_plus = f" Plus = {angka_plus:+d}"
format_pluss = f" Plus = {angka_pluss:+.3f}"

print(format_plus)
print(format_pluss)
print(format_min)

# Mmeformat Persen , menggunakan methods (:%) , (2) untuk mengambil angka 0 yang diinginkan bisa diubah sesuai keinginan
persentase = 0.045
format_persen = f" Persent = {persentase:.2%}"

print(format_persen)

# Melakukan operasi aritmatika di dalam placeholder
harga = 1000000
jumlah = 5

format_string = f"Harga total = Rp. {harga*jumlah:,}"
print(format_string)

harga = 1000000
jumlah = 50000
format_string = f"Harga total = Rp. {harga+jumlah:,}"
print(format_string)

harga = 1000000
jumlah = 50000
format_string = f"Harga total = {harga//jumlah}"
print(format_string)

harga = 1000000
jumlah = 50000
format_string = f"Harga total = {harga-jumlah:,}"
print(format_string)

# Format angka lain (Binary, Octal , Hexadecimal)

angka = 255
format_binary = f"Binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexadesimal = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexadesimal)