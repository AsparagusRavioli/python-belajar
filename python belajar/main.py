import time
start_time = time.time()


print("hello world")
a = 10
b = 100

print(" Nilai a*b = ", a*b)

nilai_y = 15000
juta10 = 1000000
Nilaiz = 18,5

a = 100
x = 1000
Dikit = 10

print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai Dikit = ", Dikit)
print(Nilaiz)



"akso belum madang multiline"

a = 20

print("nilai a = ", a)
print(time.time() - start_time, "detik")
print("Nilai a = ", a)
b = x
print("nilai b = ", b)

#data yang tidak ada koma (integer)
data_integer = 1
print("data : ", data_integer)
print("- bertipe :",type(data_integer))
#data yang ada koma(float)
data_float = 2 
print("data : ", data_float)
print("- bertipe :",type(data_float))
#data yang mengunakkan huruf atau #,$dll (string)
data_string = "ikan bawal"
print("data : ", data_string)
print(" bertipe :",type(data_string))
#data yang berisi Biner True/False(Boolean)
data_boolean = "true"
print("data : ", data_boolean)
print(" bertipe :",type(data_boolean))

#Bilangan Khusus

#Bilangan Kompleks
data_complex = complex(5,6)
print("data :", data_complex)
print("- bertipe : ", type(data_complex))

#Tipe data dari bahasa c

from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ", data_c_double)
print(" bertipe :",type(data_c_double))

#Belajar Casting
#Merubah basah satu tipe ke tipe lain 
# Tipe data = int,float,str,bool
print("=====INTEGER=====")
data_int = 9
print("data : ", data_int, "type = ",type(data_int))

data_int = int(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0
print("data : ", data_int, "type = ",type(data_int))
print("data : ", data_str, "type = ",type(data_str))
print("data : ", data_bool, "type = ",type(data_bool))

print("=====Float=====")
data_float = 9.9
print("data : ", data_float, "type = ",type(data_float))

data_int = int(data_float) # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai float = 0
print("data : ", data_int, "type = ",type(data_int))
print("data : ", data_str, "type = ",type(data_str))
print("data : ", data_bool, "type = ",type(data_bool))


print("=====Bool=====")
data_bool = False;
print("data : ", data_bool, "type = ",type(data_bool))

data_int = int(data_bool) # akan dibulatkan ke bawah
data_str = str(data_bool)
data_float = bool(data_bool) # akan false jika nilai =
print("data : ", data_int, "type = ",type(data_int))
print("data : ", data_str, "type = ",type(data_str))
print("data : ", data_float, "type = ",type(data_float))

print("=====STRING=====")
data_str = "1"
print("data : ", data_str, "type = ",type(data_str))

data_int = int(data_str) # String Harus Angka
data_float = float(data_str) # String Harus Angka
data_bool = bool(data_str) # False Jika string kosong
print("data : ", data_int, "type = ",type(data_int))
print("data : ", data_bool, "type = ",type(data_bool))
print("data : ", data_float, "type = ",type(data_float))

INPUT USER

data_str = str(input("Masukan Nama  :"))
print("data : ", "type = ", type(data_str))

data_int = int(input("Masukan Angka :"))
print("data : ", "type = ", type(data_int))

data_bool = bool(int(input("Masukan angka atau nama :")))
print("data : ",data_bool, "type = ", type(data_bool))





