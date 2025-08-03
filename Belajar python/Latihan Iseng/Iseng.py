import datetime as dt

tanggal = dt.date.today()

print(f"""
Tanggal : {tanggal}      
Hari \t: {tanggal:%A}
""")

nama = input("Masukan Nama mu! ")

if nama == "ekso":
    print("wow ekso")
elif nama == "botek":
    print("aish")
elif nama == "anya":
    print("biutuipul")
elif nama == "solmayo":
    print("shibal vro")
else:
    print("ga diajak brok")
