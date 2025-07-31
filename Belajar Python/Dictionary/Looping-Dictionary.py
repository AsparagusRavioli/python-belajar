# Belajar Looping Di Dicitonary

# Looping dictionary
teman_teman= {
    'rev':'revtuy',
    'so':'amin',
    'as':'asparagus',
    'king':'anasnasnas'
}

# Looping First Try (Yang keluar adalah keynya)
print(10*"=","Looping For","="*10)
for teman in teman_teman:
    print(teman)
    
# Operator untuk mengambil items/ iterables
# Menggunakan ---> .Keys
print(10*"=","Keys","="*10)
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))
    
# Values , mengambil iterables dari values  

print(10*"=","Value","="*10)
values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)
    
# items , mengambil iterables dari items
items = teman_teman.items()
print(items)

for item in teman_teman:
    print(item)
    
# Menggunakan gabungan antara keys , values , dan items

for key,value in teman_teman.items():
    print(f"Key : {key} | Value : {value} ")