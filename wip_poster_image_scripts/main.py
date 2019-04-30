import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots(figsize = (10,8))

#generate random walk on ZxZ
np.random.seed(0)

x_points = [0]
y_points = [0]
colors = ["red", "green", "blue", "yellow"]
n = 300

for i in range(n):
    x_points += [x_points[-1] + np.random.choice([-1,1])]
    y_points += [ y_points[-1] + np.random.choice([-1,1])]


plt.rcParams['font.sans-serif'] = 'Helvetica'


#remove top and right spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

#make integer ticks
x_ticks = list(range(0, 20, 1))
y_ticks = list(range(0, 12, 1))
plt.xticks(x_ticks)
plt.yticks(y_ticks)

x =  list(range(0,10))
y =  list(range(0,10))

xv, yv = np.meshgrid(x, y)
plt.scatter(xv, yv)

#u0 = np.meshgrid(list(range()), list(range()))

#plt.title("History")
############################################################
#PLot a bunch of arrows to show path direction
for t, (xt ,yt) in enumerate(zip(x_points, y_points)):
    #print(t,xt,yt)
    if t < n:
        plt.arrow(x_points[t], y_points[t], x_points[t+1] - x_points[t], y_points[t+1] - y_points[t], color = (colors[t%4]), head_width = 0.12, length_includes_head = True,
        edgecolor = None)


##############################################




fig.text(0.5, 0.02, '$t$', fontsize=20, fontweight='black', color = '#333F4B')
fig.text(0.02, 0.5, '$\omega(t)$', fontsize=20, fontweight='black', color = '#333F4B')
plt.show()
