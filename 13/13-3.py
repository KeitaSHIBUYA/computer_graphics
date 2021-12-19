import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, pi, sqrt

n = 100
x = np.linspace(0, 2*pi, n)
y = np.linspace(0, 2*pi, n)
X, Y = np.meshgrid(x, y)

# (u, v) = \nabla -cos(X)*cos(Y)    Pre-calculate u and v manually.
###  Calculate u  ###
z = sin(X) * sin(Y)

# Plot
plt.contour(X, Y, z, 10, cmap = 'Greens')
plt.show()