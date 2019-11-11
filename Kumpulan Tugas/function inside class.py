class MobilCustom():
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

    
mobil1 = MobilCustom(warna='pink', tahun=2010, model='X')
mobil2 = MobilCustom(warna='navy', tahun=2018, model='Z')
print(mobil1.model)
print(f'apakah jadul?', mobil1.jadul()) # --> how to call method inside class
print(mobil1.spek_mobil())
