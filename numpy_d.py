import numpy as np

l = [1,2,3,4,5]
a = np.array(l)

# print(l,type(l))
# print(a,type(a))
# print(a.ndim)
# print(a+a,2*a,np.sqrt(a))

# b = np.array([[1,2],[-1,-2]],ndmin=5)
# print(b,b.ndim)

c = np.array(
    [
        [
            [1,2],
            [3,4]
        ],
        [
            [5,6],
            [1,1]
        ]
    ]
)
# print(c[0][1][0])
# print(c[0,1,0])
# print(c[0][1][0] == c[0,1,0])

# print(c.shape)

# c1 = c.reshape(1,8)
# print(c1)
# c2 = c.reshape(-1)
# print(c2)

# for x in c:
#     print(x)

# for x in np.nditer(c):
#     print(x)

# one = np.where(c == 1)
# print(one)

# s = np.sort(c.reshape(-1))
# print(s)

# d = np.linspace(1,100,5)
# print(d)

e = np.arange(1,5)
# print(e)
# print(np.prod(e))
# print(np.cumprod(e))
# print(np.diff(e))


# print(np.lcm(3,5))
# print(np.lcm.reduce([2,5,10]))

# print(np.gcd(3,5))
# print(np.gcd.reduce([2,5,10]))

# print(np.unique([1,1,2,3,4,5,2,3,5]))

arr1,arr2 = [1,2,3],[2,3,4] 

# print(np.union1d(arr1,arr2))
# print(np.intersect1d(arr1,arr2))
print(np.setdiff1d(arr1,arr2))