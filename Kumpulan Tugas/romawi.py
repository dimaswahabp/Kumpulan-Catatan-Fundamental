#  ------------------------ Selasa, 5 November 2019 -----------------------------------

#### Romawi ####
# Tugas

romanDict = {
    'M' : 1000,
    'CM': 900,
    'D' : 500,
    'CD': 400,
    'C' : 100,
    'XC': 90,
    'L' : 50,
    'XL': 40,
    'X' : 10,
    'IX': 9,
    'V' : 5,
    'IV': 4,
    'I' : 1
}

def romanNum(param):
    newString = ''
    while param >= 1:
        for i in list(romanDict.values()):
            newString += (int(param/i) * list(romanDict.keys())[list(romanDict.values()).index(i)])
            param = param % i
    print(newString)

# romanNum(int(input('Masukkan angka : ')))

def numRom(param):
    angka = 0
    while param != romanDict:
        for i in len(param):
            x = param[i]
            y = param[i+1]
            a = romanDict.get(x)
            b = romanDict.get(y)
            if a >= b:
                angka += a
            elif x < y:
                z = b - a
                angka += z
    print(angka)
                
abc = list(input('Masukkan romawi : '))
numRom(abc)
# x = list(input('Masukkan romawi : '))

# print(x)

# y = x[1]
# print(y)

z = romanDict.get('X')
# print(z)