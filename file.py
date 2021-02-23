''' READ '''

# f = open("Dersler/sayilar.txt","r")
# r = f.read()
# print(r)

# sayilar = [float(x) for x in r.split("\n")]
# print(sayilar)

# f.close()

''' APPEND '''

# dosya = open("Dersler/sayilar.txt","a")
# dosya.write("\n Wisharedom")
# dosya.close()

# d = open("Dersler/sayilar.txt","r")
# oku = d.read()
# print(oku)
# d.close()


''' WRITE '''

yeni_dosya = open("Dersler/yeni.txt","w")
for i in range(10):

    yeni_dosya.write("Wisharedom Python Dersleri " + str(i) + "\n")

yeni_dosya.close()

y = open("Dersler/yeni.txt","r")
oku_y = y.read()
print(oku_y)
y.close()