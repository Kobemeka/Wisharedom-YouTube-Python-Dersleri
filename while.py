stop = 10
i = 0
# while i < stop:
#     print(i)
#     i = i + 1


while i < 20:
    i += 0.5
    if i % 2 == 0:
        print(str(i) + ' çift sayıdır')
    elif i % 2 == 1:
        print(str(i) + ' tek sayıdır')
    else:
        print(str(i) + ' tam sayı değildir')