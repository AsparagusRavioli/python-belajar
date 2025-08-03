# Belajar Menggunakan List --- LIST ---

## Data list Menggunakan Kurung siku ---> []

print(10*"=","Data Numbers/Integer",10*"=")
# Kumpulan Data Numbers 
data_int =[1,2,3,4,5,6,7,8,9,10]
print(data_int)

print(10*"=","Data String",10*"=")
# Kumpulan Data String
data_str = ["akso","revtuy","aspragus"]
print(data_str)

print(10*"=","Data Boolean",10*"=")
# Kumpulan Data Boolean
data_boolean = ["True","False","True","True"]
print(data_boolean)

print(10*"=","Cara Alternatif Membuah Sebuah List",10*"=")
## Cara Alternatif Membuat Sebuah List
data_range = range(0,12,2) # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

print(10*"=","Membuat List Dengan For Loop, List Comperehension",10*"=")
# Membuat list dengan for loop ,list comperehension
list_pake_for =[i for i in range(0,10)]
print(list_pake_for)

print(10*"=","Membuat List Dengan For Loop, List Comperehension , menggunakan pangkat",10*"=")
# Membuat list dengan for loop ,list comperehension , Menggunakan Pangkat / dijadikan kuadrat
list_pake_for =[i**3 for i in range(0,10)] # Menggunakan ** di samping i , (i**3)
print(list_pake_for)

print(10*"=","Menggunakan for dan if",10*"=")
# List Pake for Pake if
list_pake_for_if =[i for i in range(0,10) if i != 5] # Menggunakan ** di samping i , (i**3)
print(list_pake_for_if)

print(10*"=","Menggunakan list for , if dan modulus",10*"=")
# list pake for dan modulus

print(10*"=","Menggunakan list for , if dan modulus \nGenap",10*"=")
# Genap
list_pake_for =[i for i in range(0,10) if i%2 ==0]# Menjadi Genap
print(list_pake_for)

print(10*"=","Menggunakan list for , if dan modulus \nGanjil",10*"=")
# Ganjil
list_pake_for =[i for i in range(0,10) if i%2 !=0]# Menjadi Genap
print(list_pake_for)