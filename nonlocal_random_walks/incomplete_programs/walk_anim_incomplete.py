import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import delta_calc as dc

num_walks = 4
steps = 40
tail = 10
paths = dc.gen_walk_coords(num_walks, steps)
fig, ax = plt.subplots()
ax = plt.axis([-50,50,-50,50])


for i in range(num_walks):
    dots = plt.scatter(paths[i][0][0:tail], paths[i][1][0:tail])


# redDot, = plt.plot([0], [np.sin(0)], 'ro')
#
# def animate(i):
#     redDot.set_data(i, np.sin(i))
#     return redDot,


def animate(t):
    for i in range(num_walks):
        dots.set_data(paths[i][0][t:t+tail], paths[i][1][t:t+tail])
        return dots,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames = range(steps - tail), \
                                      interval=10, blit=True, repeat=True)

plt.show()
