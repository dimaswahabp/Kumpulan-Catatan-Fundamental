def y(a):
    return len(a)

a = ['Andi', 'Budi', 'Caca']
x = map(y, a)
print(list(x))

a = ['Cokelat', ' Melon', 'Nangka']
b = ['Apel', 'Jeruk', 'Nanas']
def combi(a, b):
    return a+' '+b

x = map(combi, a, b)
print(list(x))