#VARIABLES
nama = 'Andi'
usia = 12       # integer
tinggi = 189.3  # float
jomblo = False  # boolean



#STRING
# macam cara print kata
print("Jum'at")
print('Jum\'at')

#\t untuk tab
print('Purwadhika\tSchool')

# \n untuk enter
print('Purwadhika\nSchool')

# menggabungkan variabel string dengan kata
print(nama + ' School')
print(nama, 'School')

# str menjadikan selain string menjadi string
print('Saya ' + nama + ' usia ' + str(usia))
print('Saya', nama, 'usia', usia)

# %s reference to string yg di %, %d reference to digit yg di %
print('Saya %s usia %d' % (nama, usia))

# {} reference to yg di dalem .format
print('Saya {} usia {}'.format(nama, usia))

# f
print(f'Saya {nama} usia {usia}')

# variable string jadi berhuruf besar atau kecil
print(nama.lower())
print(nama.upper())

# ngecek sebuah variabel string hurufnya capital atau engga
x = 'hahaha'
print(x.islower())
print(x.isupper())

print(nama.lower().isupper())
print(nama.upper().islower())

# len untuk ngecek jumlah karakter dalam variabel string sampe terakhir
print(len(nama))
print(len(nama) + 5)

# [diisi nomor urutan] untuk ngecek huruf di urutan itu dalam sebuah variabel string
print(nama[0])
print(nama[2])

# pake : buat ngecek huruf dari urutan start sampe stop
print(nama[0:2])
print(nama[1:len(nama)])

# start : stop : step
print(nama[1 : len(nama) : 2])

# kalau pake -(minus) ngitungnya mulai dari kata terakhir
print(nama[-1])
print(nama[len(nama) - 1])

# pake .index buat ngecek huruf tertentu ada diurutan berapa dalam sebuah variabel string
print(nama.index('d'))

# pake .replace buat ganti karakter
print(nama.replace('An', 'Un'))

x = 12
x = 13
print(x)

x = 12
x = x + 13
print(x)

nama = 'Purwadhika Startup & Coding School'
print(len(nama.replace(' ', '')))