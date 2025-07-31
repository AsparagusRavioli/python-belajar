# Latihan percabangan , Bellajar membuat kalkulator seerhana

# Kalkulator sederhana

print(20*"=")
print("kalkulator sederhana")
print(20*"=")

angka_1 = float(input("Masukan angka 1 = "))
operator = input("Operator Kalkulator (+,-,x,/) ")
angka_2 = float(input("Masukan angka 2 = "))


# Percabangan

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah : {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah : {hasil}")
elif operator == "x":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah : {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah : {hasil}")
else:
    print("Masukan angka nya yang bener dong !")
    
print("Akhir dari program kalkulator")