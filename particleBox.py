import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')

def particle_in_a_box(L,N):
    x_values = []
    y_values = []
    XC = L/2
    kn = (N*math.pi)/L
    for x in range(L):
        for y in range(L):
            x_values.append(x)
            y_values.append(y)
    def f(x,y):
        return (((2/L)*(np.sin(kn*(x-XC+L/2)))**2)*((2/L)*(np.sin(kn*(y-XC+L/2)))**2))
    X,Y = np.meshgrid(x_values,y_values)
    Z = f(X,Y)
    ax.contour3D(X,Y,Z,50)
    plt.show()
    '''for angle in range(0,360):
        ax.view_init(30,angle)
        plt.draw()
        plt.pause(0.001)'''


particle_in_a_box(50,5)
