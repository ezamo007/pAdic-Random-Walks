import numpy as np
import math
import matplotlib.pyplot as plt

np.random.seed(87)

level = lambda r: math.ceil(-math.log2(1.0-r))

def gen_delta(level):
    leg1 = [(level-i, -level) for i in range(2*level)]
    leg2 = [(level, level-i) for i in range(2*level)]
    leg3 = [(-level+i, level) for i in range(2*level)]
    leg4 = [(-level, -level+i) for i in range(2*level)]

    legs = leg1+leg2+leg3+leg4
    index = np.random.randint(8*level)

    return legs[index]

n = 100
steps = 4

x_fin = []
y_fin = []
for i in range(n):
    for j in range(steps):
        temp_x = 0
        temp_y = 0
        r = np.random.random()
        l = level(r)
        delta = gen_delta(l)
        temp_x += delta[0]
        temp_y += delta[1]

    x_fin += [temp_x]
    y_fin += [temp_y]

plt.scatter(x_fin, y_fin)
plt.show()
