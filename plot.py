import matplotlib.pyplot as plt
import numpy as np
import random

# noise = np.array([random.random()*100 for _ in range(100)])
# n2 = np.array([random.random()*100 for _ in range(100)])

# x = np.array([x for x in range(1,101)])

# plt.subplot(1,2,1)

# plt.plot(x,noise,"b.:",ms=5,mec="k",mfc="w",label="plot noise")
# plt.subplot(1,2,2)
# plt.plot(n2,label="noise - 2")

# # plt.scatter(x,n2,label="scatter noise")

# plt.title("Gürültü Grafiği",loc='left')
# plt.xlabel("x - ekseni")
# plt.ylabel("y - ekseni")
# plt.legend()
# plt.grid(axis = "both")
# plt.show()

'''marker'''
# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# 'x'	X		
# '+'	Plus		
# 's'	Square	
# 'h'	Hexagon	

'''renkler'''
# 'r'	Red	
# 'g'	Green	
# 'b'	Blue	
# 'c'	Cyan	
# 'm'	Magenta	
# 'y'	Yellow	
# 'k'	Black	
# 'w'	White	

'''line'''
# '-'	Solid line	
# ':'	Dotted line	
# '--'	Dashed line	
# '-.'	Dashed/dotted line

# zar = np.array([random.randint(1,6) for z in range(60)])
# plt.hist(zar)

# p = np.array([10,11,6,9])
# plabels = np.array(["A","B","C","D"])
# plt.pie(p,labels = plabels)
# plt.show()

from mpl_toolkits import mplot3d

z = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(z)
x = np.cos(z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot3D(x,y,z)
ax.scatter(x**2,y**3,z)
plt.show()