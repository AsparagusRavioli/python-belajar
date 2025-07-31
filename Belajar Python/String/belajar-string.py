data="ini adalah string"
print(data)
print(type(data)) 

# Cara membuat Sebuah string

'''
 1. Dengan Menggunakan Single Qoute '...'
 2. Dengan Menggunakan Double Qoute "..."
'''
# Single Qoute (')
data = 'Ini Menggunakan single qoute'
print(data)

# Double Qoute ("")
data = "Ini Menggunakan double qoute"
print(data)

# Menggunakan Double dan Single qoute secara bersamaan ("'...'") / ('"..."')
data = '"Ini Menggunakan double dan single qoute"'
print(data)

data = "'Ini Menggunakan double dan single qoute'"
print(data)

# Menggunakan double qoute , karna didalamnya ada single qoute
print("ini adalah hari jum'at")

# Menggunkan tanda backlash (\)

# Membuat (') Menjadi String
print('mari sholat jum\'at')
print('g\'day isn\'t it?')

# Menggunakan backlash (\\)
print("C:\\folder\\ucup")
print('C:\\folder\\ucup')

# Menggunakan Tab (\t) , Menjadi jauh
print("ucup\totong, menjadi berjauhan")
print("ucup\t\t\totong,  semakin berjauhan")

# Menggunakan Backspace (\b) , menjadi dekat
print("ucup \botong, menjadi berdekatan")

# Menggunakan Newline (\n) , menjadi terpisah membuat barisan baru
print("baris pertama. \nbaris kedua. \nbaris ketiga.")# LF -> line feed -> unix , macos , linux
print("baris pertama \rbaris kedua") # CR -> Carriage return -> commodore , acorn ,lisp
print("baris pertama \r\nbaris kedua") # CRLF -> Line feed carriage return -> Dipakai oleh windows

# 3. String  Literal atau Raw

# Hati-Hati
print("C\new folder") # Akan salah pathnya

# Menggunakan RAW (r),semua yang didalam single atau double qoute akan dianggap string / di print
print(r"C\new folder")

# Multiline Literal String , Akan dianggap string isi di dalamnya ("""""")
print("""
    Nama : farel
    umur : 100 tahun
    kelas : kelas
    karbu : pe 28
    klep : 28/24
""")

# Multiline Literal String Dan raw , gabungan antara Mulltiline Dan Raw
print(r"""
    Nama : farel
    umur : 100 \\tahun
    website : www..https.com/youkiyub
""")

