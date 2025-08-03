# Operasi Dictionary

data_dict = {
    'yen':'yen yer oyen',
    'meng':'meng tekomeng komeng',
    'sibu':'sibu si abu-abu'
}

# Panjang Dictionary
lendict = len(data_dict)
print(f"Panjang data dict : {lendict}")

# Mengecek key exist atau tidak
key = "yen"
checkkey = key in data_dict
print(f"apakah {key} ada di data_dict: {checkkey}")

# Mengakses value (read) dengan --> get
print(data_dict.get("yen"))
print(data_dict.get("kumis")) # Akan None karna tidak ada di dalam data/dictionary nya
print(data_dict.get("kumis","Maaf key tidak ditemukan"))# Merubah None Menjadi kata diinginkan

# Mengupdate data 
data_dict['yen'] = "Oyen si rakus"
print(data_dict)
# Bisa juga menambahkan data baru
data_dict["cal"] = "calico mewing"
print(data_dict)

# Menambah data , yang lebih simple
data_dict.update({"cal":"calico singlet"})
print(data_dict)

data_dict.update({"mew":"si mewing"}) # Kalau data tidak ada , akan langsung di add dan terupdate
print(data_dict)

# Mendelete data pad dictionary --> (del)
del data_dict["cal"]
print(data_dict)