# Belajar Nested List

data_list_biasa = [1,2,3,4,5]
print(f"Ini list biasa/normal : \n{data_list_biasa}")

# List Didalam List ygy
data_0 = [1,2,3]
data_1 = [4,5,6,7,8]

list_2D = [data_0,data_1,data_list_biasa,9,10] # list di dalam list
print(f"Ini list di dalam list ygy : \n{list_2D}") # list di dalam list

# Contoh penggunaan list di dalam list

peserta_0 = ["oyen",1,"jantan"]
peserta_1 = ["komeng",3,"jantan"]
peserta_2 = ["siabu",4,"betina"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"Peserta : \n{list_peserta}")

for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")
    

# Dengann Reference, ada beberapa kendala yang terjadi ketika mengcopy 

list_copy = list_peserta.copy()
print(f" ini list copy : {list_copy}\n")
peserta_0[0] = "siewew"
print(f"Peserta : \n{list_peserta}")
print(f" ini list copy : {list_copy}\n")
