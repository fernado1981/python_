# Librería scikit-learn para implementar regresión lineal simple:
#### Descargaremos un set de datos relacionado al consumo de combustible y a la emisión del dióxido de Carbono en autos.  Luego, separaremos nuestros datos en un set de entrenamiento y en otro set de prueba, crearemos un modelo utilizando un set de entrenamiento, se evaluará utilizando el set de prueba para finalmente usar el modelo para predecir valores desconocidos
### Importando paquetes Necesarios:

    import matplotlib.pyplot as plt
    import pandas as pd
    import pylab as pl
    import numpy as np
    %matplotlib inline

### Descargando los Datos:
#### Para descargar los datos, usaremos !wget desde IBM Object Storage.
    
    !wget -O FuelConsumption.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv

#### ¿Sabías? Cuando se trata de Machine Learning, seguro trabajarás con grandes datasets (juego de datos). Entonces, ¿dónde podrás guardar esos datos? IBM ofrece una oportunidad única para las empresas, con 10 Tb de IBM Cloud Object Storage: Sign up now for free

##### Understanding the Data
#### FuelConsumption.csv:
#### Hemos descargado el dataset de consumo de combustible, FuelConsumption.csv, el cual contiene ratings específicos al consumo de combustible y emisiones de dióxido de carbono para aquellos vehículos ligeros en la venta minorista dentro de Canadá. Dataset source

    MODELYEAR e.g. 2014
    MAKE e.g. Acura
    MODEL e.g. ILX
    VEHICLE CLASS e.g. SUV
    ENGINE SIZE e.g. 4.7
    CYLINDERS e.g 6
    TRANSMISSION e.g. A6
    FUEL CONSUMPTION in CITY(L/100 km) e.g. 9.9
    FUEL CONSUMPTION in HWY (L/100 km) e.g. 8.9
    FUEL CONSUMPTION COMB (L/100 km) e.g. 9.2
    CO2 EMISSIONS (g/km) e.g. 182 --> low --> 0
   
### Leyendo los datos:
    df = pd.read_csv("FuelConsumption.csv")
    #un vistazo dentro del set de datos
    df.head()
    
### Exploración de Datos:
    # Tengamos primero una exploración descriptiva de nuestros datos.
    # Sumarizar los datos
    df.describe()
### Seleccionemos algunas características para explorar más en detalle:
    cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
    cdf.head(9)
### podemos dibujar cada una de estas características:
    viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
    viz.hist()
    plt.show()
### Ahora, comparemos estas características anteriores con la emisión de carbono, para ver cuán lineal es la regresión:
    plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
    plt.xlabel("FUELCONSUMPTION_COMB")
    plt.ylabel("Emission")
    plt.show()
    
    plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()
    
## Creando el set de datos de entrenamiento y de el prueba:
#### Train/Test Split divide el dataseet en uno de entrenamiento y otro de pruebas, siendo excluyentes. Después de ello, entrenas con el set de entrenamiento y pruebas con el de prueba. 
#### Esto brinda una evaluación más exacta porque el set de entrenamiento no es parte de un set de datos que se usaron para entrenar datos. Refleja un escenario más real basado en problemas más actuales.
#### Esto significa que sabemos la salida de cada punto de datos del set, siendo un escenario ideal ! Y como estos datos no se usaron para entrenar el modelo, el modelo no sabe la salida de estos puntos de datos. Asi que, básicamente, es una real prueba fuera de muestra.

    msk = np.random.rand(len(df)) < 0.8
    train = cdf[msk]
    test = cdf[~msk]
    
## Modelo de Regresión Simple:
#### La Regresión Lineal cuadra con un modelo lineal de coeficientes B = (B1, ..., Bn) para minimizar la 'suma residual de cuadrados' entre la x independiente del dataset y la dependiente y por la aproximación lineal.

### Entrenar distribución de los datos:
    plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()

## Modeling
### Usando el paquete sklearn para modelar datos:
    from sklearn import linear_model
    regr = linear_model.LinearRegression()
    train_x = np.asanyarray(train[['ENGINESIZE']])
    train_y = np.asanyarray(train[['CO2EMISSIONS']])
    regr.fit (train_x, train_y)
    # The coefficients
    print ('Coefficients: ', regr.coef_)
    print ('Intercept: ',regr.intercept_)

#### son los parámetros de la recta de ajuste. 
#### Dado que es una regresión lineal simple, con 2 parámetros solamente, y sabiendo que los parámetros son la intersección y pendiente de la linea, sklearn puede estimarlas directamente a partir de los datos. 
#### Tener en cuenta que todos los datos deben estar disponibles para poder calcular los parámetros.

## Trazar las salidas
### podemos marcar la recta de ajuste sobre los datos:
    plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
    plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    
## Evaluación
#### comparamos los valores actuales y predichos para calcular la exactitud del modelo de regresión. Las métricas de la evaluación proveen un role principal en el #### desarrollo de un modelo, ya que provee conocimiento profundo en areas que necesitan mejoras.
    from sklearn.metrics import r2_score

    test_x = np.asanyarray(test[['ENGINESIZE']])
    test_y = np.asanyarray(test[['CO2EMISSIONS']])
    test_y_ = regr.predict(test_x)

    print("Error medio absoluto: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
    print("Suma residual de los cuadrados (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
    print("R2-score: %.2f" % r2_score(test_y_ , test_y) )

