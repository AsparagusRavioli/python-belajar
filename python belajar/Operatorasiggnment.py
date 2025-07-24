# Operasi Assignment

a = 5
print('Nilai a =',a)

a += 1 # Jadi seperti a = a + 1
print('Nilai a +=, Nilai a menjadi?',a)

a -= 2 # Jadi seperti a = a - 2
print('Nilai a -=, Nilai a menjadi?',a)

a *= 5 # Jadi seperti a = a * 1
print('Nilai a *=, Nilai a menjadi?',a)

a /= 4 # Jadi seperti a = a / 1
print('Nilai a /=, Nilai a menjadi?',a)


# Menggunakan Modulus dan folder division 

c = 10
print('Nilai c adalah')

b = 10
print('Nilai b adalah =')

c %= 3
print('Nilai c %=, Nilai c menjadi?',c)

b = 5
print('Nilai b adalah =')

b **= 3
print('Nilai b //=, Nilai b menjadi?',b)

# operasi bitwise
# OR
print("============OR")
c = True 
print('\nnilai c adalah?',c)
c |= False
print('nilai c |= false , nilai c adalah',c)
c = False
print('\nnilai c adalah?',c)
c |= False
print('nilai c |= false , nilai c adalah',c)


# operasi bitwise
# AND
print("============AND")
c = True 
print('\nnilai c adalah?',c)
c &= False
print('nilai c |= False , nilai c adalah',c)
c = True
print('\nnilai c adalah?',c)
c &= True
print('nilai c |= True , nilai c adalah',c)

# operasi bitwise
# XOR
print("============XOR")
c = True 
print('\nnilai c adalah?',c)
c ^= False
print('nilai c ^= False , nilai c adalah',c)
c = True
print('\nnilai c adalah?',c)
c ^= True
print('nilai c ^= True , nilai c adalah',c)

# Geser Geser
d = 0b0100
print("\nNilai d =",format(d,'04b'))
d >>= 2
print('nilai d >>= 2 , nilai d adalah',format(d,'04b'))
d <<= 1
print('nilai d <<= 1 , nilai d adalah',format(d,'04b'))




 

