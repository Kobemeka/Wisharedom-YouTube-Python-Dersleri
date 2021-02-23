'''
    Bir üniversitede toplam notu %40 etkileyen bir vize ve %60 etkileyen bir final yapılmaktadır, 60 ve üzeri not alan öğrenci bu dersten geçmektedir. 
    Tüm öğrencilerinin notlarının ayrı listeler halinde bulunduğu bir listeden her öğrencinin ortalamasını hesaplayınız.
    Kaç kişinin dersi geçtiğini bastırınız.
'''

notlar = [[40,60],[100,100],[60,60],[50,70],[75,90],[100,100]]

gecenler = 0

for i in range(len(notlar)):

    vize = notlar[i][0]
    final = notlar[i][1]

    puan = vize * 0.4 + final * 0.6
    
    if puan >= 60:
        gecenler += 1

print(gecenler)
    