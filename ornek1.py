# Kullanıcıdan alınan bir sayı listesinin istenilen ortalamasını bulun.

liste = eval(input("Bir sayı listesi giriniz: "))
s = 0
for i in range(len(liste)):
    s = s + liste[i]
# sum_liste = sum(liste)
ortalama = s/len(liste)
print(ortalama)