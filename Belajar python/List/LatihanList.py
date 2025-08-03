# Latihan Membuat List

# Program list Buku

list_buku = []
while True:
    print("Masukan data buku")
    judul = input("Judul Buku \t:")
    penulis = input("Nama Penulis \t:")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print("\n\n","="*10,"Data Buku","="*10,)
    print("No. | Judul | Penulis ")
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]} ")
        
    print("\n\n","="*10)
    apalanjut = input("Apa kah ingin melanjutkan mendata buku? (y/n) ")
    
    if apalanjut == "n":
        break
    
print("Akhir Dari Program Mendata Buku")
    
