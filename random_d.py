import random

# a = random.randint(1,6)
# print(a)

# b = random.random()
# print(b)

# l = ["A","B","C"]

# harf = random.choice(l)
# print(harf)

# harfler = random.choices(l,[10,1,1],k=10)
# print(harfler)

# sample = random.sample(l,k = 2)
# print(sample)

# random.shuffle(l)
# print(l)

def zar(t):
    sayilar = []
    say = []

    for _ in range(t):
        sayilar.append(random.randint(1,6))

    for j in range(1,7):
        say.append(sayilar.count(j))

    return say

print(zar(6000))