import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator


def padic_abs(q,p): #q is an ordered pair
    num = q[0]
    den = q[1]
    n = 0
    m = 0
    num_divide = True
    den_divide = True

    while num_divide == True:
        if (num % (p ** n) != 0): break
        else: n += 1

    while den_divide == True:
        if (den % (p ** m) != 0): break
        else: m += 1

    return p**(m-n)

def padic_dist(q1,q2,p):
    difference = (q1[0]*q2[1]-q1[1]*q2[0], q1[1]*q2[1])
    print(padic_abs(difference, p))


#padic_dist((243,189),(210,81),3)
