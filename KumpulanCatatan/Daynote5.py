#dictionary
andi = {
    'name': 'Andi',
    'age': 22,
    'is_married': False,
    #meng-update dictionary
    'job': 'PNS',
    'cars': ['Alphard', 'Xpander', 'Innova'], #boleh berupa list
    'address': {
        'street': 'Mawar Ungu', # atau berupa dictionary yang lain
        'RT': 5,
        'RW': 2,
        'zipcode': 123456,
        'geo': {
            'lat': 121321.1212, # dalam dictionary ada dictionary lagi!
            'long': 4335435.21333
        }
    }
}

# mengambil value dari dictionary
print(andi['name'])
print(andi['age'])
print(andi['is_married'])

# mengambil value dari dictionary dengan method .get()
print(andi.get('name'))
print(andi.get('age'))
print(andi.get('is_married'))

#mengakses dictionary dalam dictionary
andi['address']['geo']

#update
# andi = 25000000
# andi['salary']


# andi.update({'no_ktp': 1234567890})
# andi['no_ktp']

# if, elif, else

# if True:
#     print(True)
# elif False:
#     print(False)

x = 100
ab = 5

if ab < 4:
    print('salah')
if ab == 5:
    print('benar')


jomblo = False; nganggur = False

if jomblo and nganggur:
    print('Anda jomblo pengangguran')
elif jomblo and not nganggur:
    print('Anda kurang piknik')
elif not jomblo and nganggur:
    print('Anda harus cari kerja')
elif not jomblo and not nganggur:
    print('Anda orang sibuk')