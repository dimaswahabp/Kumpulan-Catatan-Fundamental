# dictionary
andi = { 
    'name' : 'Andi',
    'age' : 22,
    'is_married' : False,
    'job' : 'PNS',
    'cars': [ 'Alphard', 'Xpander', 'Innova'],
    'address': {
        'street' : 'Mawar Ungu',
        'RT': 5,'RW': 121, 'Kecamaten':'X',
        'zipcode': 123445,
        'geographic':{
            'lat': 111.1,
            'lng': 65.89
        }
    }
}

andi['salary'] = 25000000
andi.update({'no_ktp':12344456668})
print(andi['address']['zipcode'])
print(list(andi))
print(list(andi.keys()))
print(list(andi.values()))
print(type(andi))


# print(andi['name'])
# print(andi['age'])
# print(andi['is_married'])
# print(andi.get('name'))
# print(andi.get('age'))
# print(andi.get('is_married'))

# andi['name'] = 'Budi'
# print(andi)