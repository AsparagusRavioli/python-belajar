# Belajar Looping list dan Enumerate 

# Looping dari list

# For Loop
print(10*'=','For Loop',10*'=')

kumpulan_angka = [4,3,5,2,6,1]

for angka in kumpulan_angka:
    print(f"angka : {angka}")
    
peserta = ["oyen","komeng","siabu","siewew","zero","sunny"]

for nama in peserta:
    print(f"Nama Peserta : {nama}")
    
    
# For Loop Dan Range
# Sama dengan For Loop Namun bedanya Lebih panjang dan sedikit ribet
print(10*'=','For Loop dan Range',10*'=')

kumpulan_angka = [4,3,5,2,6,1,100,50]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"Angka : {kumpulan_angka[i]}")
    
    
# While
print(10*'=','While Loop',10*'=')

kumpulan_angka = [1,2,1000,4,3,5,2,6,1]

panjang = len(kumpulan_angka)
i = 0

while i < panjang :
    print(f"Angka : {kumpulan_angka[i]}")
    i += 1


# Cara yang lebih mudah !!! , Menggunakan list compeherension
# List compeherension , [print(f"Data = {i}" ) for i in data] atau [print(i) for i in data]
print(10*'=','List comperehension',10*'=')

data = ["oyen",1,2,3,"kasep"]
[print(f"Data = {i}" ) for i in data]

# Angka kuadrat
angka = [1,2,1000,4,3,5,2,6,1]
angka_kuadrat = [i**2 for i in angka]
print(f"Angka kuadrat : {angka_kuadrat}")

# Enumerate
# Cara yang lebih rapih , dan bisa mendaptakan index dan data sekaligus
data_list = ["oyen",1,2,3,"kasep"]

for index,data in enumerate(data_list):
    print(f"Index = {index} , data = {data}")
