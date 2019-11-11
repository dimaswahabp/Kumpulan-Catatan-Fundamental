# NUMBER LANJUTAN
x = 12
x = 13

# Dibawah ini perhitungannya akan terus terhubung
x += 2      # x = x + 2
x -= 2      # x = x - 2
x *= 2      # x = x * 2
x /= 2      # x = x / 2
print(x)



# MULTIPLE VARIABLE VALUE
x = 'abcdefghijklmnopqrstuvwxyz'
# start : stop : step
print(x[0:len(x):2])
print(x[:len(x):2])
print(x[::2])

# 'in' dipake buat ngecek sebuah karakter ada di sebuah variable apa engga
print('12' in x)
print('g' in x)
# 'count' dipake buat ngitung jumlah karakter dalam sebuah variable
print(x.count('g'))

#contoh
x = 'Kuku Kakiku Sungguh Kaku Sekali'
cari = 'k'

print(cari in x.lower())
print(x.lower().count(cari))



# List
x = ['Andi', 'Budi', 'Caca', 123, True]
print(type(x))
# nampilin elemen keberapa yg mau ditampilin
print(x[0])
print(x[len(x) - 1])
print(x[-1])

# contoh
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
print(hari[1])

# Sekarang hari Rabu, hari apakah 100 hari lagi?
now = 'Senin'; brpHari = 100

iNow = hari.index(now)
sisaHari = brpHari % len(hari)
hariYgDicari = hari[(iNow + sisaHari) % 7]
print(f'{brpHari} hari dari hari {now} adalah hari {hariYgDicari}')



# '.append' buat nambahin elemen di urutan terakhir sebuah list
hari.append('senin2')
print(hari)
# '.insert' buat masukin elemen di urutan yg kita pengen dalam sebuah list
hari.insert(4, 'senin3')
print(hari)

# '.remove' buat hilangin elemen tertentu disebuah list
hari.remove('senin2')
print(hari)
# 'pop' buat hilangin elemen tertentu dari belakang list atau hilangin elemen di ururtan yg dipengen
hari.pop()
print(hari)
hari.pop(2)
print(hari)
# '.clear' buat ngilangin semua elemen list
hari.clear()
print(hari)

hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
# '.sort' buat ngeurutin listnya
hari.sort()
print(hari)
# cara ngebalikin urutan yg udah disort
hari.sort(reverse = True)
print(hari)
# cara ngebalikin urutan list
hari.reverse()
print(hari)
hari[::-1]
print(hari)
reversed(hari)
print(hari)



# menjadikan string jadi list
x = 'abcde'
print(list(x))
# mereverse list yg berasal dari string
print(list(reversed(x)))



x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# buat ngecopy sebagian elemen dari list lain menjadi list baru
y = x[::2].copy()
print(y)
# buat ngegabungin beberapa elemen didalam sebuah list
print(x + y)
# buat memultiple elemen didalam sebuah list
print(y * 2)



# membuat list didalam list
z = [
    [1, 2, 3, 4],
    [5, 6, 7],
    [8, 9]
]
# buat ngambil elemen di dalam elemen
print(z[0][1])



a = [1, 2, 3]   # disebut 'list'
b = (1, 2, 3)   # disebut 'tuple'
print(type(b))
# tuple = immutable (kekal atau abadi. Isisnya ga bisa kita ubah)
print(tuple(a)) # ngeubah list menjadi tuple
print(list(a))  # ngeubah tuple menjadi list