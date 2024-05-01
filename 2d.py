Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
... import numpy as np
... degree=160
... a=1
... x = np.arange(-10,10,0.01)
... y = np.arange(-10,10,0.01)
... x,y=np.meshgrid(x,y)
... v=np.power(x,2)+np.power(y,2)+np.cos(degree*np.pi/180)*np.sqrt(np.power(x+a,2)+np.power(y,2))*np.sqrt(np.power(x-a,2)+np.power(y,2))-np.power(a,2)
... plt.contour(x,y,v,0)
... plt.grid(True)
... plt.xlabel('x')
... plt.ylabel('y')
... ax=plt.gca()
... ax.set_aspect(1)
... ax.spines['right'].set_color('none')        
... ax.spines['top'].set_color('none')
... ax.xaxis.set_ticks_position('bottom')
... ax.spines['bottom'].set_position(('data', 0))
... ax.yaxis.set_ticks_position('left')
... ax.spines['left'].set_position(('data', 0))
