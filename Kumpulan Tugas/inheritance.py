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