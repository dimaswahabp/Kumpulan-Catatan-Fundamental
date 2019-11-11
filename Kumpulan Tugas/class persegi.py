class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        self.luas = self.sisi ** 2
        self.keliling = self.sisi * 4
        
persegi1 = Persegi(4)
print(vars(persegi1))