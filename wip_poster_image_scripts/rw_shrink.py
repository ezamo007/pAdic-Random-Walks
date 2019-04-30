import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize = (10,8))

#generate random walk on ZxZ
np.random.seed(0)

x_points = [0]
y_points = [0]
colors = ["red", "green", "blue", "yellow"]
n = 99999

for i in range(n):
    x_points += [x_points[-1] + np.random.choice([-1.0/n,1.0/n])]
    y_points += [ y_points[-1] + np.random.choice([-1.0/n,1.0/n])]

    plt.plot(x_points, y_points)
    if i % 20 == 0:
        plt.savefig(str(int(i/100))+".png")
plt.rcParams['font.sans-serif'] = 'Helvetica'

#remove top and right spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')






fig.text(0.5, 0.02, '$t$', fontsize=20, fontweight='black', color = '#333F4B')
fig.text(0.02, 0.5, '$\omega(t)$', fontsize=20, fontweight='black', color = '#333F4B')
plt.show()
