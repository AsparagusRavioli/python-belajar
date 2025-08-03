data = ['ipo','api','ipu']
print(data)


data.pop()
print(f"Data terakhir yang diremove : {data}")


data.remove("api")
print(f"data yang dihiliangkan : {data}")


data.insert(2,"kanjut")
print(f"Data yang ditambahkan : {data}")

data_tambahan = ['imin','umun','emen']
print(f"awal : \n{data_tambahan}")
data.extend(data_tambahan)
print(f"Data yang digabungkan : \n{data}")


data.remove("imin")
print(f"data gabungan yang di hapus : \n{data}")

data_awal = ['amin','imun']
print(data_awal)

data_pengikut = data_awal
print(data_pengikut)

data_awal[1] = "siitem"
print(data_awal)

data_duplikat = data_awal.copy()

print(f"data yang dibuat baru : \n{data_duplikat}")

data_duplikat[0] = "dombgars"
data_duplikat.insert(2,"Risol mayo")

print(f"addres a = {data_awal}")
print(f"addres b = {data_pengikut}")
print(f"addres c  = {data_duplikat}")