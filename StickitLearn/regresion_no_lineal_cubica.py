import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5.0, 5.0, 0.1)

##Puede ajustar la pendiente y la intersección para verificar los cambios del gráfico
y = 1 * (x ** 3) + 1 * (x ** 2) + 1 * x + 3
y_noise = 20 * np.random.normal(size=x.size)
ydata = y + y_noise
plt.plot(x, ydata, 'bo')
plt.plot(x, y, 'r')
plt.ylabel('Variable dependiente')
plt.xlabel('Variable indepdendiente')
print(plt.show())