# Fungsi argument default

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya):

# Contoh 1
def say_nama(nama = "kamu"):
    '''Fungsi dengan default argument'''
    print(f"Hello {nama}")
    
say_nama("dudung")

# Contoh 2
def sapa_dia(nama,pesan = "apa kabar"):
    '''Fungsi dengan satu input biasa, dan satu default argument'''
    print(f"Hai {nama}, {pesan}")
    
sapa_dia("asep" , "mau kemana sep?")
sapa_dia("jekoy")

# Contoh
def hitung_pangkat(angka, pangkat): #// Bisa juga mengunakan pangkat = angka(1,2,3,4....)
        hasil = angka**pangkat
        return hasil
    
print(hitung_pangkat(2,5))

hasil = hitung_pangkat(pangkat = 3 , angka = 5)
print(hasil)

# Contoh 4

def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))