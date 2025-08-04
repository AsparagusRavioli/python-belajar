'''Anonymous dan Lambda fungsi'''

# Menuggunakan lambda
# output = lambda argument:expression
kuadrat = lambda angka:angka**2
print(f"Hasil lambda kuadrat : {kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"Hasil lambda pangkat : {pangkat(10,2)}")

# Sort menggunakan lambda 
data_list = ["Kanya","anya","oyeng"]
data_list.sort(key=lambda nama:len(nama))
print(data_list)

# filter 
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
data_angka = list(filter(lambda angka:angka<10,data_angka))
print(f"ini adalah data lambda : {data_angka}")

# Kasus Genap
data_genap = [1,2,3,4,5,6,7,8,9,10,11,12]
data_genap = list(filter(lambda angka:(angka%2==0),data_genap))
print(f"ini adalah data genap lambda : {data_genap}")

# Kasus ganjil 
data_ganjil = [1,2,3,4,5,6,7,8,9,10,11,12]
data_ganjil = list(filter(lambda angka:(angka%2!=0),data_ganjil))
print(f"ini adalah data genap lambda : {data_ganjil}")

# Kelipatan 3
data_3 = [1,2,3,4,5,6,7,8,9,10,11,12]
data_3 = list(filter(lambda angka:(angka%3==0),data_3))
print(f"ini adalah data genap lambda : {data_3}")

# Menggunakan currying
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat1 = {pangkat2(5)}")
pangkat2 = pangkat(5)
print(f"pangkat1 = {pangkat2(10)}")
print(f"pangkat bebas = {pangkat(4)(5)}")



