''' Fungsi *args'''

# Memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan beratnya {berat}")
    
fungsi("oyen",70,5)

# Menggunakan data list
def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan beratnya {berat}")
    
fungsi(["kyomeng",85,7])

# Kenalan dengan *args --> args = argument

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan beratnya {berat}")
    
fungsi("syiabu",100,30)
    
    
# Studi kasus

def tambah(*data): #(*data) bisa dubah namanya menjadi apa saja
    output = 0
    for angka in data:
        output += angka
        
    return output

hasil = tambah(1,5,7,10)
print(f"Hasil : {hasil}")
    
    
    
