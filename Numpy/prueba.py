import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3, 4, 5])
print("El tipo es: ", type(a))
print("los datos son de tipo: ", a.dtype)

mean_a = a.mean()
print("la media de los datos del arreglo es:", mean_a)

np.linspace(0, 2, 4)
x = np.linspace(0.2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
