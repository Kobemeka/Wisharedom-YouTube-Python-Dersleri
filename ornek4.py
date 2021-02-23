''' Faktöriyel hesaplayan bir fonksiyon yazınız. '''

# def factoriyel(n):
#     if n == 0:
#         return 1
#     elif n>0:
#         return n * factoriyel(n-1)
#     else:
#         return "Sayı negatif olmayan bir sayı olmalı!"

# print(factoriyel(0))


''' Tabanı ve kendisi verilen sayıyı 10 tabanına dönüştürün.
Taban sadece 2'den 9'a kadar olan tam sayılar ve 16 olabilir. '''

def taban(sayi,taban):
    if taban >= 2 and taban <= 9:

        y = 0

        for k in range(len(sayi)):
            y = y + int( sayi[ len( sayi ) - k - 1 ] ) * ( taban ** k )
                
        return y
    elif taban == 16:
        n = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
        y = 0
        
        for k in range(len(sayi)):
            y = y + n [ sayi[ len( sayi ) - k - 1 ].upper() ]  * (taban ** k )
        return y
        
    else:
        return "Taban 2-9 aralığında olmalı!"

print(taban("0101",2))