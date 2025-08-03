# Belajar copy n pop dicitionary

# Copy dictionary

teman_teman= {
    'rev':'revtuy',
    'so':'amin',
    'as':'asparagus',
    'king':'anasnasnas'
}

friends = teman_teman.copy()
print(f"Teman-teman : \n{teman_teman}")
print(f"friends : \n{friends}")

teman_teman['so'] = "si akso bolos bae"
print(f"Teman-teman : \n{teman_teman}")
print(f"friends : \n{friends}")

# Pop Dictionary
datarev = friends.pop("rev") # Mentrasfer data friends ke ----> datarev
print(f"data rev = {datarev}\n")
print(f"friends : \n{friends}\n")

# PopItem Dictionary (item yang terakhir ajyah)
dataterakhir = friends.popitem() # Akan mengambil item yang paling belakang  di dictionary
print(f"data terakhir = {dataterakhir}\n")
print(f"friends : \n{friends}\n")