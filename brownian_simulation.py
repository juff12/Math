from math import sqrt
from scipy.stats import norm
import numpy as np
from pylab import show
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

# Process parameters
delta = 0.25
dt = 0.1

# Inital condition
x0 = 0.0

# Generates instance of Brownian motion
# x0: initial conditions of brownian motion
# n: number of steps to take
# dt: the time step
# delta: speed of brownian motion
# out: output array for results
def brownian(x0, n, dt, delta, out=None):
    x0 = np.asarray(x0)
    
    # for each element in x0 generate a sample of n numbers from a norm dist
    r = norm.rvs(size=x0.shape + (n,), scale=delta*sqrt(dt))
    
    # Create output array if out == None
    if out is None:
        out = np.empty(r.shape)
        
    # computes brownian motion by forming the cumulative sum of random samples
    np.cumsum(r, axis=-1, out=out)
    
    # add the initial condition
    out += np.expand_dims(x0, axis=-1)
    
    return out

#1D simulation of brownian motion
# delta: Wiener process param
# T: total time
# N: Number of steps
# m: Number of realizations to generate
# x0: Initial values of x
def simulation_1D(delta, T, N, m, x0, fig):
    ax = fig.add_subplot(231)
    # Time step size
    dt = T / N
    # Create an empty array to store the realizations
    x = np.empty((m,N+1))
    # Initial values of x
    x[:,0] = x0

    brownian(x[:,0], N, dt, delta, out = x[:,1:])

    t = np.linspace(0.0, N*dt, N+1)
    for k in range(m):
        ax.plot(t, x[k])
        
    ax.set_title('1D Brownian Motion')
    ax.set_xlabel('t')
    ax.set_ylabel('x')
    ax.grid(True)
    
#2D simulation of brownian motion
# delta: Wiener process param
# T: total time
# N: Number of steps
# m: Number of realizations to generate
# x0: Initial values of x
def simulation_2D(delta, T, N, m, x0, fig):
    ax = fig.add_subplot(232)
    # Time step size
    dt = T / N
    # Create an empty array to store the realizations
    x = np.empty((m,N+1))
    # Initial values of x
    x[:,0] = x0

    brownian(x[:,0], N, dt, delta, out = x[:,1:])

    # plot 2D trajectory
    ax.plot(x[0], x[1])
    
    # mark start and end points
    ax.plot(x[0,0], x[1,0], 'go')
    ax.plot(x[0,-1], x[1,-1], 'ro')
    
    ax.set_title('2D Brownian Motion')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.axis('equal')
    ax.grid(True)

# 3D simulation of brownian motion
# delta: Wiener process param
# T: total time
# N: Number of steps
# m: Number of realizations to generate
# x0: Initial values of x
def simulation_3D(delta, T, N, m, x0, fig):
    # plots the figure at location 2, 2, 3
    ax = fig.add_subplot(2, 3, 3, projection='3d')
    # Time step size
    dt = T / N
    # Create an empty array to store the realizations
    x = np.empty((m,N+1))
    # Initial values of x
    x[:,0] = x0

    brownian(x[:,0], N, dt, delta, out = x[:,1:])
    # 3D data points (uses first 3 realizations)
    x_data, y_data, z_data = x[:3,:]
    ax.plot3D(x_data, y_data, z_data)
    ax.set_title("3D Brownian Motion")



# Wiener process param
delta = 0.25
# total time
T = 10.0
# Number of steps
N = 500
# Number of realizations to generate (must be greater than 3 for 3D to work)
m = 20
# Initial values of x
x0 = 0

fig = plt.figure(1)


# Note that each simulation runs on a different set of random data

simulation_1D(delta,T,N,m,x0,fig)

simulation_2D(delta,T,N,m,x0,fig)

simulation_3D(delta,T,N,m,x0,fig)

show()