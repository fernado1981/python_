from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import wget as wget
from sklearn import linear_model

# obtenemos los datos
url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv'
wget.download(url, 'FuelConsumption.csv')

# leemos los las cinco primeras filas de los datos
df = pd.read_csv("FuelConsumption.csv")
# un vistazo dentro del set de datos
print(df.head())

# vemos una descripción de los datos
print(df.describe())

# imprimimos las nueve primeras filas de los datos ('ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS')
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
print(cdf.head(9))

print(cdf.hist())
print(plt.show())

# comparación
plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("CO2EMISSIONS")
plt.ylabel("CO2EMISSIONS")
print(plt.show())

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
print(plt.show())

# Creando el set de datos de entrenamiento y de el prueba
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

# Modelo de Regresión Simple
# Entrenar distribución de los datos:
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
print(plt.show())

regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x, train_y)
# The coefficients
print('Coefficients: ', regr.coef_)
print('Intercept: ', regr.intercept_)

# evaluacion:
test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)

print("Error medio absoluto: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Suma residual de los cuadrados (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_, test_y))
