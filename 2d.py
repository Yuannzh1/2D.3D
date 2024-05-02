import matplotlib.pyplot as plt
import numpy as np

# Define the value of degree and a
degree = 160
a = 1

# Create an array of x and y values
x = np.arange(-10, 10, 0.01)
y = np.arange(-10, 10, 0.01)

# Create a grid of x and y values
x, y = np.meshgrid(x, y)

# Define the implicit equation
v = np.power(x, 2) + np.power(y, 2) + np.cos(degree*np.pi/180) * np.sqrt(np.power(x + a, 2) + np.power(y, 2)) * np.sqrt(np.power(x - a, 2) + np.power(y, 2)) - np.power(a, 2)

# Plot the contour of the implicit equation at v=0
plt.contour(x, y, v, 0)

# Add labels and grid
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')

# Set aspect ratio and adjust spines
ax = plt.gca()
ax.set_aspect(1)
ax.spines['right'].set_color('none')        
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# Show the plot
plt.show()
