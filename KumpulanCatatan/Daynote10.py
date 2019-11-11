#10.1.1 How to make class
class Mobil:
    warna = 'merah'
    tahun = 2010

        
mobil1 = Mobil()
print(mobil1.warna)
print(vars(mobil1))

#10.1.2 How to make class properties
class MobilCustom():
    def __init__(self, warna, tahun):
        self.color = warna
        self.year = tahun
        
mobil1 = MobilCustom(warna='pink', tahun=2010)
mobil2 = MobilCustom(warna='navy', tahun=2018)
print(mobil1.color)
print(mobil1.year)


class Mobil2():
    def __init__(self, warna, tahun, model):
        self.color = warna
        self.year = tahun
        self.model = model
        
mobil1 = Mobil2(warna='pink', tahun=2010, model=['A','B'])
mobil2 = Mobil2(warna='navy', tahun=2018, model=['C','D'])
print(mobil1.model)
print(mobil2.model)

class Mobil3():
    def __init__(self, warna, tahun, model):
        self.color = warna
        self.year = tahun
        self.model = model
        
    def jadul(self):
        if self.year < 2010:
            return True
        else:
            return False
    
    def spek_mobil(self):
        return 'Warna mobil {0}, tahun mobil {1}, model mobil {2}'.format(self.color.upper(), self.year, self.model.upper())

#10.1.3 How to add function inside a class   
mobil1 = Mobil3(warna='pink', tahun=2010, model='X')
mobil2 = Mobil3(warna='navy', tahun=2018, model='Z')
print(mobil1.model)
print(f'apakah jadul?', mobil1.jadul()) # --> how to call method inside class
print(mobil1.spek_mobil())


'''
class Mobil:
    def __init__(self, warna, duduk):
        self.color = warna
        self.seat = duduk


class Hatcback(Mobil): # --------- Cara 1
    pass

class Sedan(Mobil): # ------------ Cara 2
    def __init__(self, warna, duduk):
        X.__init__(self, warna, duduk)
        
class Car(Mobil): # -------------- Cara 3 (dengan menambahkan property baru)
    def __init__(self, warna, duduk, gps, sound_sys, bel):
        super().__init__(warna, duduk)
        self.gps = gps
        self.sound_sys = sound_sys
        self.bel = bel

mobil1 = Mobil('Black', 4)
car1 = Car('Pink', 8, True, 'Simbada', True)
print(mobil1.color, mobil1.seat)
print(car1.color, car1.seat, car1.gps, car1.sound_sys, car1.bel)

print(vars(car1)) # --------- cara menampilkan semua variable
print(car1.__dict__) # ------ cara lain menampilkan semua variable

car1.velg = '18 inch'
print(vars(car1))
delattr(car1, 'velg') # ------ Tidak untuk menghapus property yang ada di Class
print(vars(car1))

del car1.color
print(vars(car1))

data_new_lambda = list(map(lambda x: Student(x['nama'], x['usia']),student_data))
print(data_new_lambda[0].nama)
print(data_new_lambda[0].usia)
'''
