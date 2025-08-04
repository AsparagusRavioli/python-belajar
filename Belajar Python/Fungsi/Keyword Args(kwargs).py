'''Keyword **kwargs fungsi'''

def fungsi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    
    print(f"{nama} punya tinggi {tinggi} dan beratnya {berat}")
    
fungsi(nama="jemew",tinggi=181,berat=60)

# Studi kasus

def math(*args,**kwargs): # Bisa menyatukan args dan kwargs
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")
            
    return output


hasil = math(1,2,3,4,option="tambah")
print(f"Hasil jumlah : {hasil}")


hasil = math(1,2,3,4,option="kali")
print(f"Hasil jumlah : {hasil}")
    