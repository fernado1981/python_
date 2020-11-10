<a name='top'></a>
[Principal](../README.md)<br/>

[Documentación])<https://www.interactivechaos.com/python/function/traintestsplit>


[Api_Post](READMEPOST.md) | [Api_Get](READMEGET.md)  | [Tuplas](READMETupleSet.md) | [Listas](READMELIST.md) | [Diccionarios](READMEDIC.md) | [Selenium](../Selenium/README.md)


*[scikit-learn -> regresión lineal multiple](#multiple)*<br/>
*[scikit-learn -> regresión polinómica](#polinomica)*<br/>
*[scikit-learn -> regresión no lineal](#noLineal)*<br/>
*[scikit-learn -> regresión logística](#RegrasionLogistica)*<br/>

<a name='lineal'></a>
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

# Librería scikit-learn para implementar regresión lineal multiple:
### Importar paquetes necesarios:
    import matplotlib.pyplot as plt
    import pandas as pd
    import pylab as pl
    import numpy as np
    %matplotlib inline
### Downloading Data:
    !wget -O FuelConsumption.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv
### Reading the data in:
    df = pd.read_csv("FuelConsumption.csv")
    # Dale un vistazo al conjunto de datos
    df.head()
### Seleccionemos algunas características:
    cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
    cdf.head(9)
### Tracemos los valores de las emisiones con respecto al tamaño del motor:
    plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()

## Creating train and test dataset
#### La división tren/prueba implica dividir el conjunto de datos en conjuntos de formación y de pruebas respectivamente, que son mutuamente excluyentes. Después de lo cual, usted entrena con el equipo de entrenamiento y prueba con el equipo de prueba. Esto proporcionará una evaluación más precisa de la precisión fuera de la muestra, ya que el conjunto de datos de la prueba no forma parte del conjunto de datos que se ha utilizado para entrenar los datos. Es más realista para los problemas del mundo real.
    msk = np.random.rand(len(df)) < 0.8
    train = cdf[msk]
    test = cdf[~msk]
#### Train data distribution
    plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()
    
    
<a name='multiple'></a>
*[scikit-learn -> regresión lineal](#lineal)*<br/>
*[scikit-learn -> regresión no lineal](#noLineal)*<br/>
*[scikit-learn -> regresión polinómica](#polinomica)*

## Multiple Regression Model: 
#### Cuando hay más de una variable independiente presente, el proceso se denomina regresión lineal múltiple. Lo bueno aquí es que la regresión lineal múltiple es la extensión del modelo de regresión lineal simple.
    from sklearn import linear_model
    regr = linear_model.LinearRegression()
    x = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
    y = np.asanyarray(train[['CO2EMISSIONS']])
    regr.fit (x, y)
    # The coefficients
    print ('Coefficients: ', regr.coef_)

## Ordinary Least Squares (OLS)
#### OLS es un método para estimar los parámetros desconocidos en un modelo de regresión lineal. OLS elige los parámetros de una función lineal de un conjunto de variables explicativas minimizando la suma de los cuadrados de las diferencias entre la variable objetivo dependiente y las previstas por la función lineal. En otras palabras, intenta minimizar la suma de errores cuadrados (SSE) o el error cuadrado medio (MSE) entre la variable objetivo (y) y nuestro resultado previsto ( ℎ𝑎𝑡ℎ𝑎𝑡𝑦 ) en todas las muestras del conjunto de datos.

#### OLS puede encontrar los mejores parámetros usando los siguientes métodos: - Resolución analítica de los parámetros del modelo mediante ecuaciones de forma cerrada - Utilizando un algoritmo de optimización (Descenso de Gradiente, Descenso de Gradiente Estocástico, Método de Newton, etc.)

#### Prediction:
    y_hat= regr.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
    x = np.asanyarray(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
    y = np.asanyarray(test[['CO2EMISSIONS']])
    print("Residual sum of squares: %.2f"
      % np.mean((y_hat - y) ** 2))

    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % regr.score(x, y))


<a name='polinomica'></a>
*[scikit-learn -> regresión lineal](#lineal)*<br/>
*[scikit-learn -> regresión lineal multiple](#multiple)*<br/>
*[scikit-learn -> regresión no lineal](#noLineal)*<br/>

## Regresión polinómica:
#### Implementar una Regresión Polinómica. Descargaremos un set de datos relacionado al consumo de combustible y a la emisión del dióxido de Carbono en autos. Luego, separaremos nuestros datos en un set de entrenamiento y en otro set de prueba, crearemos un modelo utilizando un set de entrenamiento, se evaluará utilizando el set de prueba para finalmente usar el modelo para predecir valores desconocidos

### Importando los paquetes necesarios:
    import matplotlib.pyplot as plt
    import pandas as pd
    import pylab as pl
    import numpy as np
    %matplotlib inline

### Descarga de Datos:
    !wget -O FuelConsumption.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv

### Entender los Datos:
##### FuelConsumption.csv:
#### Hemos descargado el dataset de consumo de combustible, FuelConsumption.csv, el cual contiene ratings específicos al consumo de combustible y emisiones de dióxido de carbono para aquellos vehículos ligeros en la venta minorista dentro de Canadá. Fuente de Datos

    MODELYEAR (Año del modelo) e.g. 2014
    MAKE (fabricante) e.g. Acura    
    MODEL (modelo) e.g. ILX
    VEHICLE CLASS (tipo de vehiculo) e.g. SUV
    ENGINE SIZE (tamaño del motor) e.g. 4.7
    CYLINDERS (cilindrada) e.g 6
    TRANSMISSION (transmisión) e.g. A6
    FUEL CONSUMPTION in CITY(L/100 km) (consumo en ciudad) e.g. 9.9
    FUEL CONSUMPTION in HWY (L/100 km) (consumo en carretera) e.g. 8.9
    FUEL CONSUMPTION COMB (L/100 km) (consumo mixto) e.g. 9.2
    CO2 EMISSIONS (g/km) (emisiones de dioxido de carbono) e.g. 182 --> low --> 0

### Leyendo los datos:
    df = pd.read_csv("FuelConsumption.csv")
    # observar dentro del conjunto de datos
    df.head()

### Seleccionemos algunas caracaterísticas para usar en la regresión:
    cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
    cdf.head(9)
    
### Grafiquemos los valores de emisión respecto al tamaño del motor:
    plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()
    
### Crear conjunto de datos de entrenamiento y pruebas:
#### Hay que dividir el conjunto en dos, el de entrenamiento y el de pruebas, los cuales son mutuamente excluyentes. Despues de hacerlo, deberá entrenar con el conjunto de entrenamiento y hacer pruebas con el conjunto de pruebas.
    msk = np.random.rand(len(df)) < 0.8
    train = cdf[msk]
    test = cdf[~msk]

## Regresión Polinómica:
#### En ocasiones la tendencia de los datos no es lineal si no que tiene una apariencia curva. Para estos caso podemos usar los métodos de Regresión Polinómica. De hecho, existen diversos tipos de regresión que pueden ser usados para ajustarse de acuerdo a la apariencia de los datos, como puede ser la regresión cuadratica, cúbica, etc. Puede haber tantos tipos de regresiones como grados en un polinomio.
#### La función PloynomialFeatures() de la librería Scikit-learn maneja un nuevo conjunto de características del conjunto original.

    from sklearn.preprocessing import PolynomialFeatures
    from sklearn import linear_model
    train_x = np.asanyarray(train[['ENGINESIZE']])
    train_y = np.asanyarray(train[['CO2EMISSIONS']])

    test_x = np.asanyarray(test[['ENGINESIZE']])
    test_y = np.asanyarray(test[['CO2EMISSIONS']])

    poly = PolynomialFeatures(degree=2)
    #    fit_transform toma los valores de x e imprime una lista de los datos que van desde la magnitud 0 a la 2 (ya que hemos seleccionado que nuestro polinómio   sea de segundo grado).
    train_x_poly = poly.fit_transform(train_x)
    train_x_poly

#### Ahora podemos manejar el problema como si se tratara de una 'regresión lineal'. Por lo tanto, esta regresión polinomica se considera como un caso especial de regresión lineal múltiple. Puede utilizar la misma mecánica para resolver dicho problema.
### Usemos la función LinearRegression() para resolver:
    clf = linear_model.LinearRegression()
    train_y_ = clf.fit(train_x_poly, train_y)
    # los coeficientes 
    print ('Coefficients: ', clf.coef_)
    print ('Intercept: ',clf.intercept_)

### Grafiquemoslo:
    plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
    XX = np.arange(0.0, 10.0, 0.1)
    yy = clf.intercept_[0]+ clf.coef_[0][1]*XX+ clf.coef_[0][2]*np.power(XX, 2)
    plt.plot(XX, yy, '-r' )
    plt.xlabel("Engine size")
    plt.ylabel("Emission")

### Evaluación:
    from sklearn.metrics import r2_score

    test_x_poly = poly.fit_transform(test_x)
    test_y_ = clf.predict(test_x_poly)

    print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
    print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
    print("R2-score: %.2f" % r2_score(test_y_ , test_y) )
    
### uso de la regresión polinomica de tercer grado(cúbica) para mayor precisión:
    poly3 = PolynomialFeatures(degree=3)
    train_x_poly3 = poly3.fit_transform(train_x)
    clf3 = linear_model.LinearRegression()
    train_y3_ = clf3.fit(train_x_poly3, train_y)
    # The coefficients
    print ('Coefficients: ', clf3.coef_)
    print ('Intercept: ',clf3.intercept_)
    plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
    XX = np.arange(0.0, 10.0, 0.1)
    yy = clf3.intercept_[0]+ clf3.coef_[0][1]*XX + clf3.coef_[0][2]*np.power(XX, 2) + clf3.coef_[0][3]*np.power(XX, 3)
    plt.plot(XX, yy, '-r' )
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    test_x_poly3 = poly3.fit_transform(test_x)
    test_y3_ = clf3.predict(test_x_poly3)
    print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y3_ - test_y)))
    print("Residual sum of squares (MSE): %.2f" % np.mean((test_y3_ - test_y) ** 2))
    print("R2-score: %.2f" % r2_score(test_y3_ , test_y) )

<a name='noLineal'></a>
*[scikit-learn -> regresión lineal](#lineal)*<br/>
*[scikit-learn -> regresión lineal multiple](#multiple)*<br/>
*[scikit-learn -> regresión polinómica](#polinomica)*
## Regresion no lienal:
### Importando las librerías requeridas:
    import numpy as np
    import matplotlib.pyplot as plt
    %matplotlib inline

#### Las regresiones no-lineales son una relación entre variables independientes  𝑥  y una variable dependiente  𝑦  que resulta en una función no lineal. Básicamente, cada relación que no es lineal puede transformarse en una no lineal, y generalmente se representa con el polinomio de grados  𝑘  (potencia máxima de  𝑥 ).
    𝑦=𝑎𝑥3+𝑏𝑥2+𝑐𝑥+𝑑 
 
####Las funciones no lineales pueden tener elementos como exponentes, logaritmos, fracciones y otros. Por ejemplo:
    𝑦=log(𝑥)
 
#### O más complicados, como :
    𝑦=log(𝑎𝑥3+𝑏𝑥2+𝑐𝑥+𝑑)

### gráfico de la función cúbica:
    x = np.arange(-5.0, 5.0, 0.1)

    ##Puede ajustar la pendiente y la intersección para verificar los cambios del gráfico
    y = 1*(x**3) + 1*(x**2) + 1*x + 3
    y_noise = 20 * np.random.normal(size=x.size)
    ydata = y + y_noise
    plt.plot(x, ydata,  'bo')
    plt.plot(x,y, 'r') 
    plt.ylabel('Variable dependiente')
    plt.xlabel('Variable indepdendiente')
    plt.show()
    
#### Como se puede ver, esta función tiene  𝑥3  y  𝑥2  como variables independientes. También, el gráfico de esta función no es una linea directa, por lo que es una función no lineal.

## Algunas otras funciones no lineales son:
### Cuadrática 𝑌=𝑋2
    x = np.arange(-5.0, 5.0, 0.1)

    ##Se puede ajustar la pendiente y la intersección para verificar los cambios en el gráfico
    y = np.power(x,2)
    y_noise = 2 * np.random.normal(size=x.size)
    ydata = y + y_noise
    plt.plot(x, ydata,  'bo')
    plt.plot(x,y, 'r') 
    plt.ylabel('Variable dependiente')
    plt.xlabel('Variable indepdiendente')
    plt.show()

### Exponencial
#### Una función exponencial con base c se define por 𝑌=𝑎+𝑏𝑐𝑋
#### donde b ≠0, c > 0 , c ≠1, y x es cualquier número real. La base, c, es constante y el exponente, x, es una variable.
    X = np.arange(-5.0, 5.0, 0.1)

    ##Se puede ajustar la pendiente y la intersección para verificar los cambios en el gráfico
    Y= np.exp(X)
    plt.plot(X,Y) 
    plt.ylabel('Variable Dependiente')
    plt.xlabel('Variable Independiente')
    plt.show()
    
### Logarítmico
#### La respuesta  𝑦  es el resultado de aplicar el mapa logarítmico desde el valor de entrada de  𝑥  a la variable de salida  𝑦 . Es una de las formas más simples de log(): i.e. 𝑦=log(𝑥)
 
#### considerar que en vez de  𝑥 , podemos usar  𝑋 , el cual puede ser una representación polinomial de las  𝑥 's. En su forma general, se escribiría como 𝑦=log(𝑋)
    X = np.arange(-5.0, 5.0, 0.1)

    Y = np.log(X)
    plt.plot(X,Y) 
    plt.ylabel('Variable Dependiente')
    plt.xlabel('Variable Independiente')
    plt.show()
    
### Sigmoidal/Logística 𝑌=𝑎+𝑏1+𝑐(𝑋−𝑑)
    X = np.arange(-5.0, 5.0, 0.1)

    Y = 1-4/(1+np.power(3, X-2))

    plt.plot(X,Y) 
    plt.ylabel('Variable Dependiente')
    plt.xlabel('Variable Independiente')
    plt.show()
    
### Ejemplo Regresión No-Lineal:
#### Por ejemplo, intentaremos fijar un modelo no lineal a los puntos correspondientes al GDP de China entre los años 1960 y 2014. Descargaremos un set de datos con dos columnas, la primera, un año entre 1960 y 2014, la segunda, el ingreso anual de China en dólares estadounidenses para ese año.
    import numpy as np
    import pandas as pd

    #downloading dataset
    !wget -nv -O china_gdp.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/china_gdp.csv
    
    df = pd.read_csv("china_gdp.csv")
    df.head(10)
    
### Marcando el set de datos:
    plt.figure(figsize=(8,5))
    x_data, y_data = (df["Year"].values, df["Value"].values)
    plt.plot(x_data, y_data, 'ro')
    plt.ylabel('GDP')
    plt.xlabel('Year')
    plt.show()
    
### Eligiendo un modelo:
    X = np.arange(-5.0, 5.0, 0.1)
    Y = 1.0 / (1.0 + np.exp(-X))

    plt.plot(X,Y) 
    plt.ylabel('Variable Dependiente')
    plt.xlabel('Variable Independiente')
    plt.show()
    
### Construyendo el Modelo:
    def sigmoid(x, Beta_1, Beta_2):
        y = 1 / (1 + np.exp(-Beta_1*(x-Beta_2)))
        return y

### sigmoide posible:
    beta_1 = 0.10
    beta_2 = 1990.0

    #función logística
    Y_pred = sigmoid(x_data, beta_1 , beta_2)

    #predicción de puntos
    plt.plot(x_data, Y_pred*15000000000000.)
    plt.plot(x_data, y_data, 'ro')
    
### busqueda de mejores parámetros y normalizar x e y:
    # Normalicemos nuestros datos
    xdata =x_data/max(x_data)
    ydata =y_data/max(y_data)

### ¿Cómo podemos encontrar los mejores parámetros para nuestra linea?
#### podemos utilizar curve_fit la cual utiliza cuadrados mínimos no lineales para cuadrar con la función sigmoide
#### popt son nuestros parámetros optimizados.
    from scipy.optimize import curve_fit
    popt, pcov = curve_fit(sigmoid, xdata, ydata)
    #imprimir los parámetros finales
    print(" beta_1 = %f, beta_2 = %f" % (popt[0], popt[1]))
    
### Dibujamos nuestro modelo de regresión:
    x = np.linspace(1960, 2015, 55)
    x = x/max(x)
    plt.figure(figsize=(8,5))
    y = sigmoid(x, *popt)
    plt.plot(xdata, ydata, 'ro', label='data')
    plt.plot(x,y, linewidth=3.0, label='fit')
    plt.legend(loc='best')
    plt.ylabel('GDP')
    plt.xlabel('Year')
    plt.show()

###  calcular la exactitud del modelo:
    msk = np.random.rand(len(df)) < 0.8
    train_x = xdata[msk]
    test_x = xdata[~msk]
    train_y = ydata[msk]
    test_y = ydata[~msk]

    # construye el modelo utilizando el set de entrenamiento
    popt, pcov = curve_fit(sigmoid, train_x, train_y)

    # predecir utilizando el set de prueba
    y_hat = sigmoid(test_x, *popt)

### evaluation:
    print("Promedio de error absoluto: %.2f" % np.mean(np.absolute(y_hat - test_y)))
    print("Suma residual de cuadrados (MSE): %.2f" % np.mean((y_hat - test_y) ** 2))
    from sklearn.metrics import r2_score
    print("R2-score: %.2f" % r2_score(y_hat , test_y) )

<a name='RegrasionLogistica'></a>
## REGRESION LOGÍSTICA:
crear un modelo basado en datos de telecomunicaciones para predecir cuándo los clientes buscarán otro competidor de forma tal de poder tomar alguna decisión para retenerlos.

#### ¿Cuál es la diferencia entre Regresión Logística y Regresión Lineal?
Mientras la Regresión Lineal es para estimar valores continuos (ej. estimar precios de casas), no es la mejor herramienta para predecir la clase de un punto de datos observados. Para estimar la clase de punto de datos, necesitaremos una guía de lo que sería la clase más probable para ese punto de datos. Por esto, utilizamos Regresión Logística.

### Regresión Lineal:

Como sabes, la __Regresión lineal__ encuentra una función que relaciona una variable continua dependiente, _y_, con algunos predictores (variables independientes _x1_, _x2_, etc.). Por ejemplo, la regresión lineal Simple asume una función de la forma:

    𝑦=𝜃0+𝜃1∗𝑥1+𝜃2∗𝑥2+...
 

y encuentra los valores de los parámetros _θ0_, _θ1_, _𝜃2_, etc, donde el término _𝜃0_ es "intersección". Generalmente se muestra como:

    ℎθ(𝑥)=𝜃𝑇𝑋
    
La Regresion Logística es una variación de una Regresión Lineal, útil cuando la variable dependiente observada, y, es categórica. Produce una fórmula que predice la probabilidad de la clase etiqueta como una función de las variables independientes.

La regresión logística es una curva especial en forma de s a partir de tomar la regresión lineal y transformar la estimación numérica en una probabilidad

En resumen, la Regresión Logística pasa la entrada a través de las funciones logística/sigmoide pero en realidad termina tratando al resultado como una probabilidad:

<Regresion logística.png>

### Cliente churn con Regresión Logística
Una compañía de telecomunicaciones está preocupada por el número de clientes que dejan sus líneas fijas de negocio por las de competidores de cable. Ellos necesitan entender quién se está yendo. Imagina que eres un analista en esta compañía y que tienes que descubrir quién es el cliente que se va y por qué

### importamos librerías:
    import pandas as pd
    import pylab as pl
    import numpy as np
    import scipy.optimize as opt
    from sklearn import preprocessing
    %matplotlib inline 
    import matplotlib.pyplot as plt

### Acerca del set de datos:
Utilizaremos datos de las telecomunicaciones para poder predecir el cliente churn. Estos son datos históricos de clientes donde cada fila representa un cliente. Los datos son fáciles de comprender, y podrás descubrir conclusiones que puedes usar de inmediato. Generalmente, es menos caro mantener clientes que conseguir nuevos, así que el foco de este análisis es predecir los clientes que se quedarían en la compañía.
Los datos incluyen información acerca de:

- Clientes que se fueron el último mes – la columna se llama Churn
- Los servicios que cada cliente ha contratado – teléfono, líneas múltiples, internet, seguridad online, resguardo online, protección de dispositivos, soporte técnico y streaming de TV y películas
- Información de la cuenta del cliente - cuánto hace que es cliente, contrato, método de pago, facturación digital, cargos mensuales y cargos totales
- Información demográfica de los clientes – sexo, rango de edad y si tienen pareja y dependientes

### Cargar los datos Churn de la Telco:
Telco Churn es un archivo de datos ficticio que trata sobre los esfuerzos de una compañía de telecomunicaciones para reducir la huída de sus clientes. Cada caso corresponde a un cliente y se guarda información demográfica e información referente al uso del servicio. Antes de trabajar con los datos, debes utilizar la URL para obtener el archivo ChurnData.csv.

    !wget -O ChurnData.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/ChurnData.csv
    
### Cargar los Datos desde el Archivo CSV:
    churn_df = pd.read_csv("ChurnData.csv")
    churn_df.head()

### Selección y pre-procesamiento de datos:
Seleccionemos algunas características para el modelado. También cambiemos el tipo de dato del objetivo (target) para que sea un número entero (integer), ya que es un requerimiento del algoritmo skitlearn:

    churn_df = churn_df[['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip',   'callcard', 'wireless','churn']]
    churn_df['churn'] = churn_df['churn'].astype('int')
    churn_df.head()
    
### contamos el número de filas y columnas total:
    print(churn_df.count)
    
### Definamos X, e y para nuestro set de datos:
    X = np.asarray(churn_df[['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip']])
    X[0:5]
    
    y = np.asarray(churn_df['churn'])
    y [0:5]
### normalicemos el set de datos:
    from sklearn import preprocessing
    X = preprocessing.StandardScaler().fit(X).transform(X)
    X[0:5]
    
### Entrenar/Probar el set de datos:
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
    print ('Train set:', X_train.shape,  y_train.shape)
    print ('Test set:', X_test.shape,  y_test.shape)
    
### Modelando (Regresión Logística con Scikit-learn):
LogisticRegression con el package Scikit-learn. Esta función implementa regresión logística y puede usar distintos optimizadores numéricos para encontrar parámetros, a saber, ‘newton-cg’, ‘lbfgs’, ‘liblinear’, ‘sag’, ‘saga’ solvers. Puedes también encontrar más información sobre los pros y contras de estos optimizadores si buscas en internet.

La versión de Regresión Logística en, soporta regularización. Esto es, una técnica que soluciona problemas de sobreajuste en modelos de machine learning. El parámetro C indica fuerza de regularización inversa la cual debe ser un número flotante positivo. Valores más pequeños indican regularización más fuerte. Now lets fit our model with train set:

    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import confusion_matrix
    LR = LogisticRegression(C=0.01, solver='liblinear').fit(X_train,y_train)    
    LR
    
### predecir usando nuestro set de prueba:
    yhat = LR.predict(X_test)
    yhat

predict_proba devuelve estimaciones para todas las clases. La primer columna es la probabilidad de la clase 1, P(Y=1|X), y la segunda columna es la probabilidad de la clase 0, P(Y=0|X):

    yhat_prob = LR.predict_proba(X_test)
    
### Evaluación:
índice jaccard
Probemos con el índice jaccard para la evaluación de precisión. Podemos definir como jaccard al tamaño de la intersección dividida por el tamaño de la unión de dos set de etiquetas. Si todo el set de etiquetas de muestra predichas coinciden con el set real de etiquetas, entonces la precisión es 1.0; sino, sería 0.0.

    from sklearn.metrics import jaccard_similarity_score
    jaccard_similarity_score(y_test, yhat)
    
### Matriz de confusión: (Otra forma de mirar la precisión del clasificador es ver la matriz de confusión.)

    from sklearn.metrics import classification_report, confusion_matrix
    import itertools
    def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    Esta función muestra y dibuja la matriz de confusión.
    La normalización se puede aplicar estableciendo el valor `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Matriz de confusión normalizada")
    else:
        print('Matriz de confusión sin normalización')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('Etiqueta Real')
    plt.xlabel('Etiqueta Predicha')
    print(confusion_matrix(y_test, yhat, labels=[1,0]))
    
### Calcular la matriz de confusión
    cnf_matrix = confusion_matrix(y_test, yhat, labels=[1,0])
    np.set_printoptions(precision=2)
    
### Dibujar la matriz de confusión no normalizada
    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=['churn=1','churn=0'],normalize= False,  title='Matriz de confusión')
    
    
<matriz de confusion.png>
    
    print (classification_report(y_test, yhat))
    
    
    ###                precision    recall  f1-score   support

    ###           0       0.73      0.96      0.83        25
    ###           1       0.86      0.40      0.55        15

    ###   micro avg       0.75      0.75      0.75        40
    ###   macro avg       0.79      0.68      0.69        40
    ### weighted avg      0.78      0.75      0.72        40

Partiendo de la cantidad de cada sección podemos calcular la precisión y el grado(recall) de cada etiqueta:
- Precision es una medida de certeza basada en una etiqueta predicha. Se define de esta forma: precision = TP / (TP + FP)
- Recall es un grado positivo verdadero. Se define de esta forma: Recall =  TP / (TP + FN)
Por lo tanto, podemos calcular la precisión y grado de cada clase.
- F1 score: Ahora estamos en condiciones de calcular los puntajes F1 para cada etiqueta basada en la precisión y grado de cada etiqueta.
El puntaje F1 es el promedio armónico de la precisión y grado, donde un grado F1 alcanza su mejor valor en 1 (precisión y grado perfectos) y peor escenario en 0. Es una buena forma de mostrar que un clasificador tiene un buen valor tanto para la precisión como para el grado.
Y finalmente, podemos decir que la exactitud promedio para este clasificador es el promedio del score f1 para ambas etiquetas, cuyo valor es is 0.72 en nuestro caso.

### Log Loss:
Ahora, probemos log loss para la evaluación. En regresión logística, la salida puede ser que la probabilidad de cliente churn sea sí (o su equivalente 1). Esta probabilidad es un valor entre 0 y 1. Log loss( pérdida logarítmica) mida el rendimiento de un clasificador donde la salida predicha es una probabilidad de valor entre 0 y 1.

    from sklearn.metrics import log_loss
    log_loss(y_test, yhat_prob)

[Subir](#top)
