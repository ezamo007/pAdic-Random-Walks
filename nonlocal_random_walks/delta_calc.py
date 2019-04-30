import numpy as np
import math

np.random.seed(87)

#Given a number between 0 and 1, level returns 1 50% of the time, 2 25% of the time, 3 12.5% of the time... etc.
#level corresponds to the l_inf distance in Z^2.
def level(r): return math.ceil(-math.log2(1.0-r))

#Given a level, we create a list of all the possible (delta_x, delta_y) that correspond to that level,
#and then pick one at random.
def gen_delta(level):

    leg1 = [(level-i, -level) for i in range(2*level)]
    leg2 = [(level, level-i) for i in range(2*level)]
    leg3 = [(-level+i, level) for i in range(2*level)]
    leg4 = [(-level, -level+i) for i in range(2*level)]

    legs = leg1+leg2+leg3+leg4
    index = np.random.randint(8*level)

    return legs[index]

#Returns an array with n elements, each element is a pair of lists denoting the x and y coordinates of
#the nonlocal random walk on Z2.
def gen_walk_coords(num_walks = 1, steps = 500):
    paths = [] * num_walks
    for i in range(num_walks):
        temp_walk_x = [0]
        temp_walk_y = [0]
        for j in range(steps):
            r = np.random.random()
            lvl = level(r)
            delta = gen_delta(lvl)
            temp_walk_x += [temp_walk_x[-1] + delta[0]]
            temp_walk_y += [temp_walk_y[-1] + delta[1]]
            #Activate to confirm correct random walk
            #print(r,level,delta)

        paths += [[temp_walk_x, temp_walk_y]]
    return paths
