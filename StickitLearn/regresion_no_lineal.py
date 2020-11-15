import numpy as np
import pandas as pd
import wget as wget
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit

url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/china_gdp.csv'
wget.download(url, 'china_gdp.csv')

df = pd.read_csv("china_gdp.csv")
df.head(10)

# Marcando el set de datos
plt.figure(figsize=(8, 5))
x_data, y_data = (df["Year"].values, df["Value"].values)
plt.plot(x_data, y_data, 'ro')
plt.ylabel('GDP')
plt.xlabel('Year')
print(plt.show())

# Eligiendo un modelo
X = np.arange(-5.0, 5.0, 0.1)
Y = 1.0 / (1.0 + np.exp(-X))

plt.plot(X, Y)
plt.ylabel('Variable Dependiente')
plt.xlabel('Variable Independiente')
print(plt.show())


# funcion que Construye el Modelo
def sigmoid(x, Beta_1, Beta_2):
    y = 1 / (1 + np.exp(-Beta_1 * (x - Beta_2)))
    return y


# sigmoide posible
beta_1 = 0.10
beta_2 = 1990.0

# función logística
Y_pred = sigmoid(x_data, beta_1, beta_2)

# predicción de puntos
plt.plot(x_data, Y_pred * 15000000000000.)
plt.plot(x_data, y_data, 'ro')

# busqueda de mejores parámetros y normalizar x e y
xdata = x_data / max(x_data)
ydata = y_data / max(y_data)

popt, pcov = curve_fit(sigmoid, xdata, ydata)
# imprimir los parámetros finales
print(" beta_1 = %f, beta_2 = %f" % (popt[0], popt[1]))

# Dibujamos nuestro modelo de regresión:
x = np.linspace(1960, 2015, 55)
x = x / max(x)
plt.figure(figsize=(8, 5))
y = sigmoid(x, *popt)
plt.plot(xdata, ydata, 'ro', label='data')
plt.plot(x, y, linewidth=3.0, label='fit')
plt.legend(loc='best')
plt.ylabel('GDP')
plt.xlabel('Year')
print(plt.show())


msk = np.random.rand(len(df)) < 0.8
train_x = xdata[msk]
test_x = xdata[~msk]
train_y = ydata[msk]
test_y = ydata[~msk]

popt, pcov = curve_fit(sigmoid, train_x, train_y)
y_hat = sigmoid(test_x, *popt)

print("Promedio de error absoluto: %.2f" % np.mean(np.absolute(y_hat - test_y)))
print("Suma residual de cuadrados (MSE): %.2f" % np.mean((y_hat - test_y) ** 2))
print("R2-score: %.2f" % r2_score(y_hat, test_y))