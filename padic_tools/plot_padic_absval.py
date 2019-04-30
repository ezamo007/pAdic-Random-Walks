import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from calc_padic_absval import padic_abs

p = 13
z1 = 100
z2 = 50


plt.figure(figsize = [100,100])

for i in range(1,z1,1):
    for j in range(1,z2,1):
        smushed_value = 1 / (1 + np.e**(-0.5 * padic_abs((i,j),p)))
        
        plt.arrow(i-0.5,j, 1,0, width = 1 , head_width = 0, color = (1-smushed_value, smushed_value,0))
        plt.text(i,j,round(padic_abs((i,j),p),2, ), fontsize = 8 )

plt.axis((0,20,0,20))
plt.gca().invert_yaxis()
plt.gca().xaxis.tick_top()
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
#plt.savefig("aaaa.png")



plt.show()
