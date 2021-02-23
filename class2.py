class Dikdortgen:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def alan(self):
        return self.a*self.b

class Kare(Dikdortgen):
    def __init__(self,c):
        Dikdortgen.__init__(self,c,c)

d = Dikdortgen(3,4)
# print(d.alan())

k = Kare(5)
# print(k.alan())

# print(k)
# print(k+d)

class Liste:
    def __init__(self,l):
        self.l = l

    def __add__(self,diger):
        return [m + diger for m in self.l]

    def __mul__(self,diger):
        return [v * diger for v in self.l]

    def __rmul__(self,diger):
        return [v * diger for v in self.l]

    def __truediv__(self,diger):
        return [v / diger for v in self.l]

    def __str__(self):
        return str("Bu bir listedir.")

    def __int__(self):
        return sum(self.l)

liste = Liste([1,2,3])

# print(liste+3)
# print(3*liste)
# print(liste*3)
# print(liste/3)
print(liste)
print(int(liste))