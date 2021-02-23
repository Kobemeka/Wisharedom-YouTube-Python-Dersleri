# class Araba:
#     renk = "kirmizi"

# print(Araba.renk)

class Ogrenci:
    def __init__(self,isim,yas,puan):
        self.isim = isim
        self.yas = yas
        self.puan = puan
        
can = Ogrenci('can',20,3.5)
kubilay = Ogrenci('kubilay',21,3.51)

# print(can.isim,kubilay.isim)
# print(can.yas,kubilay.yas)
# print(can.puan,kubilay.puan)
# print(can.puan + kubilay.puan)

class Ders:
    def __init__(self,*args):
        self.sinif = args
    def bitir(self):
        self.sinif = ()

ders = Ders(can,kubilay)
# print(ders.sinif)
# print(ders.sinif[0].isim)
# ders.bitir()
# print(ders.sinif)

class Yarisma:
    def __init__(self,yarismaci):
        self.yarismaci = yarismaci
    def dogru(self):
        self.yarismaci.puan += 0.1
    def yanlis(self):
        self.yarismaci.puan -= 0.1
    def durum(self):
        return "4.0'a ulaşmak için kalan puan: {}".format(4.0-self.yarismaci.puan)

yarisma = Yarisma(can)
yarisma.dogru()
print(yarisma.yarismaci.puan)
print(yarisma.durum())