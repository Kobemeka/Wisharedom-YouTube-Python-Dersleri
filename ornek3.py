# Bir matrisin tersçaprazını veren bir fonksiyon yazınız.

m = [
    [1,2],
    [3,4],
    [11,-3]
]

def transpose(matris):
    y = []

    for sutun in range(len(matris[0])):
        s = []
        for satir in range(len(matris)):
            deger = matris[satir][sutun]
            s.append(deger)
        y.append(s)
    return y

t = transpose(m)
print(t)