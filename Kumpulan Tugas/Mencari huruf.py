name = 'Purwadhika Startup & Coding School'
print(name.lower().count('startup'))
print(name.lower().count('o'))

nama = 'Hari ini Hari tidak masuk sekolah'
cari = 'h'
x = nama.upper().replace(cari.upper(),'')
print(x)
# jmlCari =len(nama) - len(x)
jmlCari = int((len(nama) - len(x) / len (cari))
print (f'Jumlah Kata \'{cari}\' ada = {jmlCari} ')