import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,7,100)
y = np.random.rand(100)
z = x*y

plt.figure(figsize=(10,8))
plt.scatter(x,z,color='blue',maeker='.')
plt.show()