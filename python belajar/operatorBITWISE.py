# Operator BITWISE , operasi binery , binery

a = 9
b = 5


# Bitwsie OR (|)

c = a | b 
print("=====OR======")
print('nilai =',a,',binary',format(a,'08b'))
print('nilai =',b,',binary',format(b,'08b'))
print("============(|)")
print('nilai =',c,',binary',format(c,'08b'))


# Bitwise AND (&)
c = a & b
print("=====AND======")
print('nilai =',a,',binary',format(a,'08b'))
print('nilai =',b,',binary',format(b,'08b'))
print("============(&)")
print('nilai =',c,',binary',format(c,'08b'))

# Bitwise XOR (^)
c = a ^ b
print("=====XOR======")
print('nilai =',a,',binary',format(a,'08b'))
print('nilai =',b,',binary',format(b,'08b'))
print("============(^)")
print('nilai =',c,',binary',format(c,'08b'))

# Bitwise NOT (~)
c = ~a
print("=====NOT======")
print('nilai =',a,',binary',format(a,'08b'))
print('nilai =',b,',binary',format(b,'08b'))
print("============(~)")
print('nilai =',c,',binary',format(c,'08b'))

# Bitwise Not menggunakan Xor
c = ~a
print("=====NOT======")
print('nilai =',a,',binary',format(a,'08b'))
print('nilai =',b,',binary',format(b,'08b'))
print("============(~)")
print('nilai =',c,',binary',format(c,'08b'))
d = 0b0000001001
e = 0b1111111111
print('Nilai =',d^e,',binary',format(d^e,'08b'))


# Shifting

# Shift Right (>>)
c = a >> 2
print("=====>>======")
print('nilai =',a,',binary',format(a,'08b'))
print('nilai =',b,',binary',format(b,'08b'))
print("============(>>)")
print('nilai =',c,',binary',format(c,'08b'))

# Shift Right (<<)
c = a << 2
print("=====>>======")
print('nilai =',a,',binary',format(a,'08b'))
print('nilai =',b,',binary',format(b,'08b'))
print("============(<<)")
print('nilai =',c,',binary',format(c,'08b'))

a = 16
b = 7

c = a | b
print('nilai :',a,'binary',format(a,'08b'))
print('nilai :',b,'binary',format(b,'08b'))
print('nilai :',c,'binary',format(c,'08b'))

