# Teknik Menduplikat list

a = ["kanya","oyen","komeng"]
print(f"a = {a}")

b = a  # hanya membuat list dengan nama berbeda  , tetapi addresnya sama /isinya sama // pass by reference
print(f"b = {b}")

# Kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = "siabu"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")

# Menduplikat list dengan copy


print(" Membuat list c dengan a.copy()")
c = a.copy() # full duplicate / data baru , membuat data yang baru

print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")
print(f"addres c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(" kita ubah data 0")
c[0] = "Anya"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(" kita ubah data 1")
a[1] = "lele"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")