import matplotlib.pyplot as plt
import numpy as np

def plot_rw_prob(color):
    n = 10
    window = (-n,n,-n,n)

    for x in range(window[0],window[1]+1, 1):
        for y in range(window[2],window[3]+1, 1):

            l = max(x,y,-x,-y)

            if l == 0:
                p = 0
            else:
                p = (l*2**(l+3))**-1


            plt.arrow(x-0.3,y, 1,0, width = 1 , head_width = 0, color = (color[0], color[1], color[2],  (2*p)**(1/3)))
            plt.text(x,y,round(p,4), fontsize = 8 )

    plt.axis(window)
    # plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    #plt.savefig("aaaa.png")

    plt.show()
