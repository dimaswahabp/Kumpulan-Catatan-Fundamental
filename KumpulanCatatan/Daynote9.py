#lambda function
x = lambda a:a
x(2)

y =lambda a,b,c : a+b+c
y(2,5,1)

def my_function(x):
    return lambda a:a**x

pangkat2 = my_function(2)
pangkat3 = my_function(3)
pangkat5 = my_function(5)

print(pangkat2(4))
print(pangkat3(4))
print(pangkat5(4))

y = lambda a : True if a%2 == 0 else False
print(y(2))
print(y(3))

y = lambda a : 'Angka Genap' if a%2 == 0 else 'Angka Ganjil'
print(y(2))
print(y(3))

def z(a):
    return len(a)

a = ['Andi', 'Budi', 'Caca']
x = map(z, a)
print(list(x))

#map function
def u(a):
    return len(a)

a = ['Andi', 'Budi', 'Caca']
x = map(u, a)
print(list(x))

a = ['Cokelat', ' Melon', 'Nangka']
b = ['Apel', 'Jeruk', 'Nanas']
def combi(a, b):
    return a+' '+b

x = map(combi, a, b)
print(list(x))

x = range(11)
def kurang_lima(a):
    if a < 5:
        return False
    else:
        return True
    
y = filter(kurang_lima, x)
print(list(y))
x = [1,2,3,4,5]
y = [1,2,6,7,8]

z = filter(lambda a: a in x, y)
print(list(z))

from functools import reduce
number = [1,2,3,4]
y = reduce(lambda a, b:a*b, number)
print(y)

number = [1,2,3,4]
hasil = 1
for i in number:
    hasil *= i

print(hasil)

kata = ['ini', 'ibu', 'budi']
b = reduce(lambda a, b:a+b, kata)
print(b)

angka = [1,2,3,4]

z = list(map(lambda x:x*2, filter(lambda x:x>3, angka)))
y = list(filter(lambda x:x>3, map(lambda x:x*2, angka)))
print(z)
print(y)