
nilai = 45 

if nilai >= 82:
    print('A')
elif nilai >= 72 and nilai <= 81:
    print('B')
elif nilai >= 62 and nilai <= 71:
    print('C')
elif nilai >= 52 and nilai <= 62:
    print('D')
else:
    print('E')


x = int(input('masukkan nilai anda :')) 

if x >= 90 and x <= 100:
    print(f'nilai anda {x}adalah A')
elif x >= 85 and x <= 90:
        print(f'nilai {x} adalah B+')
elif x >= 81 and x <= 84:
        print(f'nilai anda{x} adalah B')
elif x >= 75 and x <= 80:
        print(f'nilai anda {x}adalah B-')
elif x >= 71 and x <= 74:
        print(f'nilai anda {x} adalah C')
elif x >= 60 and x <= 70:
        print(f'nilai anda{x} adalah D')
elif x >= 0 and x <= 59:
        print(f'nilai anda{x} adalah E')
else:
        print(f'niali anda{x} tidak ditemukan')