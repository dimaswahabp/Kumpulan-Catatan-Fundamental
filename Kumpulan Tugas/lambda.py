def my_function(x):
    return lambda a:a**x

pangkat2 = my_function(2)
pangkat3 = my_function(3)
pangkat5 = my_function(5)

print(pangkat2(4))
print(pangkat3(4))
print(pangkat5(4))

y = lambda a : 'Angka Genap' if a%2 == 0 else 'Angka Ganjil'
print(y(2))
print(y(3))