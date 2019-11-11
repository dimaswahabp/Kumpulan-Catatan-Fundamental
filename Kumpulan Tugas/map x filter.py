angka = [1,2,3,4]

z = list(map(lambda x:x*2, filter(lambda x:x>3, angka)))
y = list(filter(lambda x:x>3, map(lambda x:x*2, angka)))
print(z)
print(y)