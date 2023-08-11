import numpy as np
import matplotlib.pyplot as plt
import random

s = 30 #sample size
epsilon = 1

distances = []

x = [random.randint(1, 100) for n in range(s)]
y = [random.randint(1, 100) for n in range(s)] #randomizing coordinates 
xtemp = [0, 0]
ytemp = [0, 0]

def getDistances(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

plt.style.use('dark_background')


m = 1

for i in range(1, 500):
    fig, ax = plt.subplots()
    ax.set_title("Rips Complex")
    for j in range(s): #draws circles
        circle = plt.Circle((x[j], y[j]), radius=epsilon, fill=0)
        point = plt.Circle((x[j], y[j]), radius=0.5, fill=1, color="blue")
        ax.add_patch(circle)
        ax.add_patch(point)
    #then, we want to figure out all the points that are within epsilon distance of each other
    for j in range(s):
        for k in range(j + 1, s):
            if getDistances(x[j], y[j], x[k], y[k]) <= epsilon:
                xtemp = [x[j], x[k]]
                ytemp = [y[j], y[k]]
                plt.plot(xtemp, ytemp, color="blue")
            for l in range(2):
                xtemp[l] = 0
                ytemp[l] = 0
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.savefig(str(m))
    m += 1
    epsilon += 0.1