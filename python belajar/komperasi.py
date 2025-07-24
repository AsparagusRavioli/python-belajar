# belajar komparasi

# Menggunakan <,>,>=,<=,==,!=,is,is not

a = 4
b = 2

# Komparasi lebih dari (>)
print("======= Komparasi lebih dari (>)")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# Komparasi kurang dari (<)
print("======= Komparasi kurang dari (<)")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# Komparasi lebih dari sama dengan (>=)
print("======= Komparasi lebih dari (>=)")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# Komparasi kurang dari sama dengan (<=)
print("======= Komparasi  kurang dari  sama dengan(<=)")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# Komparasi  sama dengan (==)
print("======= Komparasi    sama dengan(==)")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 2
print(b,'==',2,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)

# Komparasi tidak sama dengan (!=)
print("======= Komparasi  tidak  sama dengan(!=)")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 2
print(b,'!=',2,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)

# is sebagai komparasi object identity
print("======= object identity(is)")
x = 5 # Ini adalah assignment membuat object 
y = 5 
print('nilai x = ',x,'id = ',hex(id(x)))
print('nilai y = ',y,'id = ',hex(id(y)))
hasil = x is y
print('x is y',hasil)

# is sebagai komparasi object identity
print("======= object identity(is)")
x = 5 # Ini adalah assignment membuat object 
y = 6
print('nilai x = ',x,'id = ',hex(id(x)))
print('nilai y = ',y,'id = ',hex(id(y)))
hasil = x is y
print('x is y',hasil)

# is sebagai komparasi object identity
print("======= object identity(is not)")
x = 5 # Ini adalah assignment membuat object 
y = 6
print('nilai x = ',x,'id = ',hex(id(x)))
print('nilai y = ',y,'id = ',hex(id(y)))
hasil = x is not y
print('x is not y',hasil)


# is sebagai komparasi object identity
print("======= object identity(is not)")
x = 5 # Ini adalah assignment membuat object 
y = 5
print('nilai x = ',x,'id = ',hex(id(x)))
print('nilai y = ',y,'id = ',hex(id(y)))
hasil = x is not y
print('x is not y',hasil)














