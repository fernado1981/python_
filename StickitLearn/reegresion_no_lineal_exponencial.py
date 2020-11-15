import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-5.0, 5.0, 0.1)

##Se puede ajustar la pendiente y la intersección para verificar los cambios en el gráfico
Y = np.exp(X)
plt.plot(X, Y)
plt.ylabel('Variable Dependiente')
plt.xlabel('Variable Independiente')
print(plt.show())
