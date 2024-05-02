import plotly.graph_objects as go
import numpy as np
# Creating a grid of points in 3D space using np.mgrid
# The grid spans from -2 to 2 in each dimension, with 100 points per dimension
X, Y, Z = np.mgrid[-2:2:100j, -2:2:100j, -2:2:100j]

degree=60
a=1

values =X**2+Y**2+Z**2+np.cos(degree*np.pi/180)*np.sqrt((X+a)**2+Y**2+Z**2)*np.sqrt((X-a)**2+Y**2+Z**2)-a**2
# Creating a Plotly figure
fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=0,
    isomax=0,
    #surface_fill=0.4,
    opacity=0.3,
    colorscale='blues',
    flatshading = True,
    caps=dict(x_show=False, y_show=False)
    ))
fig.show()
