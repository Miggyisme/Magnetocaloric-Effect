import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]

y = np.gradient(y,x)


plt.scatter(x,y)
plt.grid(True)
plt.show()