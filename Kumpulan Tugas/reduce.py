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