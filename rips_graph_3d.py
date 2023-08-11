import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits import mplot3d

s = 30 #sample size
epsilon = 1

distances = []

xcoords = [random.randint(1, 30) for n in range(s)]
ycoords = [random.randint(1, 30) for n in range(s)]
zcoords = [random.randint(1, 30) for n in range(s)] #randomizing coordinates 
xtemp = [0, 0]
ytemp = [0, 0]
ztemp = [0, 0]

m = 1

def getDistances(x1, y1, z1, x2, y2, z2):
    return np.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1) + (z2 - z1)*(z2 - z1))

plt.style.use('dark_background')

for i in range(1, 500):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    for j in range(s): # setting up the points
        pointRadius = 0.5
        theta = np.linspace(0, 2.*np.pi, 100)
        phi = np.linspace(0, np.pi, 100)
        xPoint = pointRadius * np.outer(np.cos(theta), np.sin(phi)) + xcoords[j]
        yPoint = pointRadius * np.outer(np.sin(theta), np.sin(phi)) + ycoords[j]
        zPoint = pointRadius * np.outer(np.ones(np.size(theta)), np.cos(phi)) + zcoords[j]
        ax.plot_surface(xPoint, yPoint, zPoint, color='b')
    #figuring out distances and drawing lines
    for j in range(s):
        for k in range(j + 1, s):
            if getDistances(xcoords[j], ycoords[j], zcoords[j], xcoords[k], ycoords[k], zcoords[k]) <= epsilon:
                xtemp = [xcoords[j], xcoords[k]]
                ytemp = [ycoords[j], ycoords[k]]
                ztemp = [zcoords[j], zcoords[k]]
                plt.plot(xtemp, ytemp, ztemp, color="blue")
            for l in range(2):
                xtemp[l] = 0
                ytemp[l] = 0
                ztemp[l] = 0
    ax.view_init(elev=20., azim=45 + (0.5 * i))
    plt.savefig(str(m))
    plt.clf()
    m += 1
    epsilon += 0.1
