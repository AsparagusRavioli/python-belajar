''' Type hints  fungsi'''

# Bentuk standar fungsi yang sudah dipelajari

'''
# Studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)
    
fungsi(3)
fungsi("komyeng")
fungsi(True)
'''

# Penggunan Type Hints
import string

def fungsi_hints(argument:int) -> str:
    output = 10**argument
    return output

hasil = fungsi_hints(2)
print(f"Hasil pangkat adalah : {hasil}")

def display(argument:str) -> str:
    print(argument)
    
display("ndut")
