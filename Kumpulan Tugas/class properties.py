lass MobilCustom():
    def __init__(self, warna, tahun):
        self.color = warna
        self.year = tahun
        
mobil1 = MobilCustom(warna='pink', tahun=2010)
mobil2 = MobilCustom(warna='navy', tahun=2018)
print(mobil1.color)
print(mobil1.year)


class MobilCustom():
    def __init__(self, warna, tahun, model):
        self.color = warna
        self.year = tahun
        self.model = model
        
mobil1 = MobilCustom(warna='pink', tahun=2010, model=['A','B'])
mobil2 = MobilCustom(warna='navy', tahun=2018, model=['C','D'])
print(mobil1.model)
print(mobil2.model)