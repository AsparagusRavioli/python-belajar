# Belajar multikeys dan nesting dicitonary

import datetime

000,7,2)
    
}
mahasiswa2 = {mahasiswa1 = {
    'nama':'risma',
    'nim':'190023',
    'sks_lulus':120,
    'beasiswa':True,
    'lahir':datetime.datetime(2
    'nama':'masri',
    'nim':'19034',
    'sks_lulus':100,
    'beasiswa':True,
    'lahir':datetime.datetime(2003,1,2)
    
}
mahasiswa3 = {
    'nama':'remas',
    'nim':'190077',
    'sks_lulus':150,
    'beasiswa':False,
    'lahir':datetime.datetime(2000,7,7)
}

# dictionary di dalam di dictionary


data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(F"{'KEY':<10} {'NAMA':<13} {'SKS':<3} {'BEASISWA':<9} {'LAHIR':<13}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    key = mahasiswa
    
    nama = data_mahasiswa[key]['nama']
    nim = data_mahasiswa[key]['nim']
    sks = data_mahasiswa[key]['sks_lulus']
    beasiswa = data_mahasiswa[key]['beasiswa']
    lahir = data_mahasiswa[key]['lahir'].strftime("%x") #.strftime("%x") karena menggunakan datetime
    
    print(F"{key:<10} {nama:<13} {sks:<3} {beasiswa:^9} {lahir:<13}")