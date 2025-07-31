# Operasi logika atau boolean

# Not , Or , And , Xor

print('=====NOT=====')
a = True
c = not a
print('data a =',a)
print('------- NOT')
print('data c =',c)


# OR (Jika salah satu True maka hasilnya True)
print('=====OR=====')
a = False
b = False
c = a or b
print(a,' or', b, '=',c)
a = True
b = False
c = a or b
print(a,' or', b, '=',c)
a = False
b = True
c = a or b
print(a,' or', b, '=',c)
a = True
b = True
c = a or b
print(a,' or', b, '=',c)

# AND (Jika salah satu False maka hasilnya False , jika hasilnya dua duanya true maka hasilnya adalah true)
print('=====AND=====')
a = False
b = False
c = a and b
print(a,' and', b, '=',c)
a = True
b = False
c = a and b
print(a,' and', b, '=',c)
a = False
b = True
c = a and b
print(a,' and', b, '=',c)
a = True
b = True
c = a and b
print(a,' and', b, '=',c)

# AND (Jika salah satu False maka hasilnya False , jika hasilnya dua duanya true maka hasilnya adalah true)
print('=====AND=====')
a = False
b = False
c = a and b
print(a,' and', b, '=',c)
a = True
b = False
c = a and b
print(a,' and', b, '=',c)
a = False
b = True
c = a and b
print(a,' and', b, '=',c)
a = True
b = True
c = a and b
print(a,' and', b, '=',c)

# XOR (Akan true jika salah satu true,sisanya false)
print('=====XOR=====')
a = False
b = False
c = a ^ b
print(a,' xor', b, '=',c)
a = True
b = False
c = a ^ b
print(a,' xor', b, '=',c)
a = False
b = True
c = a ^ b
print(a,' xor', b, '=',c)
a = True
b = True
c = a ^ b
print(a,' xor', b, '=',c)





