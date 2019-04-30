#delta_calc has 2 functions, level(r) and gen_delta(level).
import delta_calc as dc
import matplotlib.pyplot as plt
import numpy as np
import time
import os

#Making a folder in animation_images for the random walk plots.
walk_time = str(time.time())
os.mkdir("nonlocal_random_walks\\animation_images\\" +  walk_time)

#This program plots num_walks number of walks with steps step each.
def plot_rw(num_walks = 1, steps = 100):
    paths = dc.gen_walk_coords(num_walks, steps)

    for i in range(len(paths)):
        plt.plot(paths[i][0], paths[i][1])
    plt.show()



def gen_rw_animation(num_walks = 4, steps = 50, tail = 5, window = [-100,100,-100,100]):
    paths = dc.gen_walk_coords(num_walks, steps)

    for step in range(steps-tail):
        plt.grid()

        for i in range(num_walks):

            for j in range(tail):
                plt.axis(window)
                #print(paths[i][0][step+j], paths[i][1][step+j])
                plt.scatter([paths[i][0][step+j]], [paths[i][1][step+j]], alpha = j/tail, color = (i/num_walks, 1- i/num_walks, 0.5 + (0.5*i/num_walks)))

            plt.plot(paths[i][0][step:step+tail], paths[i][1][step:step+tail], linewidth = 0.5, color = (i/num_walks, 1- i/num_walks, 0.5 + (0.5*i/num_walks)))
        plt.savefig("nonlocal_random_walks\\animation_images\\" + walk_time + "\\" + str(step) + ".png")

        plt.clf()
