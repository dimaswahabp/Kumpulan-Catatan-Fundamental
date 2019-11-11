# contoh menggunakan while loop
cities = ['Jakarta', 'Bandung', 'Surabaya']
i = 0
while i < len(cities):
    print(cities[i])
    i += 1

for city in cities:
    print(city)

for i in range(0,10,4):
    print(i)
else:
    print('ok')

for i in range(0,5):
    print(i)
    if i == 3:
        break

for i in range(0,5):
    if i == 3:
        break
    print(i)
for i in range(0,5):
    if i == 3:
        continue
    print(i)
# Hai aku Lintang
# menjadi
# iaH uka gnatniL

sent = 'Hai aku Ridho'
sent_list = sent.split()
sent_rev_list = []
for word in sent_list:
    sent_rev_list.append(word[::-1])
sent_rev = ' '.join(sent_rev_list)
print(sent_rev)

morse = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..'
}