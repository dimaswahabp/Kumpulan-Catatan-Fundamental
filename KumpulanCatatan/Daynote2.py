# x = 18
# y = 2

# print(x+y)
# print(x-y)
# print(float(x*y))
# print(int(x/y))
# print(float('1234.890'))
# print(y**2)
# print(1%3)

# x = -90.321
# #print(abs(x))

# print(pow(2,3))
# print(2 ** 3)
# # akar pangkat???
# print(4 ** (1/2))
# print(27 ** (1/3))

# #MAX - MIN - Round

# print(max(1,2,3,4,5,6,7,100))
# print(min(1,2,3,4,5,6,7,8,9,.2))
# print(round(34.56079))
# print(round(34.56079, 2))
# print(round((0.1 + 0.2),1))

# #math
# import math
# print(math.pi)
# print(math.floor(3.9))
# print(math.ceil(4.9))
# print(math.sqrt(196))
# print(math.factorial(7))

# #ngitung
# kambing = 4
# Sapi = 4
# ayam = 2
# Jmlhewan = 13
# jmlkaki = 32
# kakihewan1 = 4
# kakihewan2 = 4

# Sapi = (((Jmlhewan*kakihewan1)- jmlkaki)/kakihewan1)
# kambing = Jmlhewan - Sapi

# print(Sapi)
# print(kambing)

#input 

tothewan = int (input('Ketik total hewan? :'))
totkaki = int (input('Ketik total kaki hewan? :'))
totkakiA = int (input('Ketik jumlah kaki hewan A? :'))
totkakiB =int  (input('Ketik Jumlah kaki hewan B? :'))

HewanA = int (((tothewan*totkakiB)- totkaki)/totkakiA)
HewanB = int (tothewan - HewanA)

print('hewan A =  ',HewanA, 'Hewan B = ',HewanB )

