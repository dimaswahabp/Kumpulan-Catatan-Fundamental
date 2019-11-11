# -------------------------- Jumat, 1 November 2019 -----------------------------------

# Membuat pola loop

# star = ''
# for i in range(5):
#     star += ' * '
#     print(star)


def star(x):
    star = ''
    for i in range(x):
        star = '* ' * (i + 1)
        print(star)
star(5)

def rStar(x):
    star = ''
    for i in range(x):
        star = ' * ' * (x - i)
        print(star)
# rStar(5)

#1
'''
def number(x):
    number = ''
    for i in range(x):
        angka = 1 + i
        number += str(angka) + ' '
        print(number)
number(5)
'''
#2
'''
def rNumber(x):
    number = ''
    for i in range(x):
        angka = x - i
        number = (str(angka) + ' ') * (x - i)
        print(number)
rNumber(5)
'''
#3
'''
def aNumber(x):
    number = ''
    for i in range(x):
        angka = 1 + i
        number = (str(angka) + ' ') * (1 + i)
        print(number)
aNumber(5)
'''
#4
'''
def bNumber(x):
    number = ''
    for i in range(x):
        angka = 1 + i
        number = (str(angka) + ' ') * (x - i)
        print(number)
bNumber(5)
'''
#5
'''
def cNumber(x):
    number = ''
    for i in range(x):
        angka = x - i
        number += (str(angka) + ' ')
        print(number)
cNumber(5)
'''
#6

def dNumber(x):
    z = x + 1
    for i in range(1, z):
        number = ''
        for h in range(1, (z + 1 - i)):
            number += str(z - h) + ' '
        print(number)
# dNumber(5)

#1              #3              #5
'''
1               1               5
1 2             2 2             5 4
1 2 3           3 3 3           5 4 3
1 2 3 4         4 4 4 4         5 4 3 2
1 2 3 4 5       5 5 5 5 5       5 4 3 2 1
'''
#2              #4              #6
'''
1 2 3 4 5       1 1 1 1 1       5 4 3 2 1
1 2 3 4         2 2 2 2         5 4 3 2
1 2 3           3 3 3           5 4 3
1 2             4 4             5 4
1               5               5
'''

def eNumber(x):
    for i in range(x, 0, -1):
        number = ''
        for j in range(i, 0, -1):
            number += str(j) + ' '
        print(number)
# eNumber(5)

# -------------------------- Jumat, 1 November 2019 -----------------------------------
'''
pangkat = 1
def pangkat(x, y):
    pangkat = 1
for z in range(y):
        pangkat *= x
    print(f'Jawaban dari {x} pangkat {y} adalah {pangkat}')
pangkat(2, 3)
'''
# Function yang memanggil dirinya sendiri dinamakan "Rekursif Fungsi"
def pangkatB(x, y):
    if (y == 1):
        return x
    else:
        return x * pangkatB(x, y-1)
print(pangkatB(2,3))

# Penjelasan
'''
pangkatB(2,3) = return 2 * pangkatB(2,2)        = 2 * 4 = 8
pangkatB(2,2) = return 2 * pangkatB(2,1)        = 2 * 2
pangkatB(2,1) = return 2
'''