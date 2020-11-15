import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-5.0, 5.0, 0.1)

Y = 1 - 4 / (1 + np.power(3, X - 2))

plt.plot(X, Y)
plt.ylabel('Variable Dependiente')
plt.xlabel('Variable Independiente')
print(plt.show())
