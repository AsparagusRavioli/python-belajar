# Fungsi dengan argument (input)

'''
def nama_fungsi(argument/parameter):
    badan fungsi # Template 
'''


def hello_world(nama):
    '''fungsi hello world menerimainput dengan variable nama'''
    print(f"Selamat datang wahai {nama}")
    
hello_world("ucup")
hello_world("bigsmoke")

# Program tambah

def tambah(angka_1,angka_2):
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
    hasil = angka_1 * angka_2
    print(f"{angka_1} x {angka_2} = {hasil}")
    
tambah(10,5)
tambah(1000, 7)

# List peserta

def anggota(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang hormat ter {peserta}")
        
anggota_peserta = ["kanya","oyen","asparagus"]
regutulip = ["amin","imin","umun"]

anggota(anggota_peserta)
anggota(regutulip)