
## K-Vecinos Más Cercanos (KNN):

#### En este lab, cargaremos un conjunto de datos de un cliente, adaptaremos la información y utilizaremos el algoritmo de k-vecinos más cercanos para predecir un punto de datos. ¿Qué es K-Vecinos Más Cercano?
#### Vecinos K Más Cercanos es un algoritmo para aprendizaje supervisado. Donde los datos se entrenana con puntos de datos que corresponden a su clasificación. Como un punto se predice, toma en cuenta los puntos 'K' más cercanos para determinar su clasificación

##### En este caso, tenemos puntos de datos de Clase A y B. Deseamos predecir dónde está la estrella (punto de datos de prueba). Si consideramos un valor k de 3 (3 el punto más cercano) obtendremos una predicción de Clase B. Sin embargo, si consideramos un valor k de 6, obtendremos una predicción de Clase A.

##### En este sentido, es importante considerar el valor de k. Mirando al diagrama, deberías deducir lo que es realmente un algormitmo de K Vecinos más cercanos. Tiene en cuenta los vecinos 'K' más cercano (puntos) cuando predice la clasificación de los puntos de prueba.

### Carga librerias necesarias:
    import itertools
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.ticker import NullFormatter
    import pandas as pd
    import numpy as np
    import matplotlib.ticker as ticker
    from sklearn import preprocessing
    %matplotlib inline
    
### Acerca del set de datos
##### Imagina un proveedor de telecomunicaciones que ha segmentado la base de sus clientes por servicio, categorizando a los clientes en cuatro grupos. Si los datos demográficos se pueden usar para predecir la pertenencia de grupo del envío, la compañía podría personalizar las ofertas para los prospectos. Es un problema de clasificación. O sea, dado un set de datos, con etiquetas predefinidas, necesitaremos construir un modelo para predecir la clase de un nuevo o desconocido caso.

##### Este ejemplo hace foco en datos demográficos, sean region, edad, estado civil, para predecir patrones de uso.

##### El campo objetivo (target), llamado custcat, tiene cuatro valores posibles que corresponden a los cuatro grupos de clientes, a saber: 1- Servicio Básico 2- E-Servicio 3- Servicio Plus 4- Servicio Total

##### Nuestro objetivo es construir un clasificador para predecir la clase de casos desconocidos. Utilizaremos un tipo específico de clasificación llamado K vecino más cercano.

### Descarga de set de datos:
    !wget -O teleCust1000t.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/teleCust1000t.csv
    
### Cargar Datos a partir de un archivo CSV (Valores Delimitados por Coma):
    df = pd.read_csv('teleCust1000t.csv')
    df.head()
   
### Visualización de Datos y Análisis:
    df['custcat'].value_counts()

### visualizar datos:
    df.hist(column='income', bins=50)
    
## Feature set
### Definir feature sets, x:
    df.columns

### conversion de data fame de panda a Numpy array:
    X = df[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] .values  #.astype(float)
    X[0:5]
    
    y = df['custcat'].values
    y[0:5]
    
### normalizar datos:
##### La estandarización de Datos brinda a los datos cero media y varianza de unidad, es buena práctica, especialmente para algoritmos tales como KNN el cual se basa en distancia de casos:
    X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
    X[0:5]

### Train Test Split:
##### Al margen de la exactitud de la muestra, está el porcentaje de las predicciones correctas que el modelo hace de los datos para el que no ha sido entrenado. Al hacer un entrenamiento y prueba en el mismo set de datos, de seguro tendrán baja exactitud de muestra debido a la probabilidad de estar sobre dimensionado.

##### Es importante que nuestros modelos tengan una exactitud de muestra alta porque el propósito de cualquier modelos es lograr predicciones lo más certeras posibles sobre datos no conocidos. Entonces, ¿cómo podemos mejorar la precisión? Una forma es utilizar un enfoque de evaluación llamado Train/Test Split (Entrenar/Evaluar Dividir).
##### Esta forma requiere dividir el set de datos en conjuntos de entrenamiento y prueba, los cuales son mutuamente exclusivos. Luego de ello, se entrena con el conjunto de entrenamiento y se prueba con el conjunto de prueba.

##### Este método brinda una evaluación más precisa porque el set de prueba no es parte del conjunto de datos que ha sido utilizado para entrenar los datos. Es más realista para los problemas actuales.

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
    print ('Set de Entrenamiento:', X_train.shape,  y_train.shape)
    print ('Set de Prueba:', X_test.shape,  y_test.shape)
    
### Clasificación:
### K-vecinos más cercano (K-NN)
##### Importar librería
#### Clasificador que implementa k-vecinos más cercanos.
    from sklearn.neighbors import KNeighborsClassifier
    
### Entrenamiento: k=4
    k = 4
    #Entrenar el Modelo y Predecir  
    neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)  
    neigh
    
### Predicción:
#### podemos utilizar el modelo para predecir el set de prueba:
    yhat = neigh.predict(X_test)
    yhat[0:5]
    
### Evaluación de certeza:
##### En clasificación multietiqueta, la función classification accuracy score computa la certeza del subconjunto. Esta función es igual a la función jaccard_similarity_score. Básicamente, calcula cómo se relacionan las etiquetas actuales con las etiquetas predichas dentro del set de pruebas.
    from sklearn import metrics
    print("Entrenar el set de Certeza: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
    print("Probar el set de Certeza: ", metrics.accuracy_score(y_test, yhat))
    
### probando la certeza con 10 k:
    Ks = 10
    mean_acc = np.zeros((Ks-1))
    std_acc = np.zeros((Ks-1))
    ConfustionMx = [];
    for n in range(1,Ks):
    
      #Entrenar el Modelo y Predecir  
      neigh = KNeighborsClassifier(n_neighbors = n).fit(X_train,y_train)
      yhat=neigh.predict(X_test)
      mean_acc[n-1] = metrics.accuracy_score(y_test, yhat)

    
      std_acc[n-1]=np.std(yhat==y_test)/np.sqrt(yhat.shape[0])

    mean_acc
    
### Dibujo de la certeza del modelo para diferentes números de vecinos:
    plt.plot(range(1,Ks),mean_acc,'g')
    plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)
    plt.legend(('Certeza ', '+/- 3xstd'))
    plt.ylabel('Certeza ')
    plt.xlabel('Número de Vecinos (K)')
    plt.tight_layout()
    plt.show()
    
    print( "La mejor aproximación de certeza fue con ", mean_acc.max(), "con k=", mean_acc.argmax()+1) 

## ÁRBOLES DE DECISIÓN:
En este ejercicio, aprenderás un algoritmo muy popular de machine learning llamado Árboles de Decisión. Utilizarás un algoritmo de clasificación para construir un modelo basado en datos históricos de pacientes y sus respectivos medicamentos. Luego, utilizarás el árbol de decisión recién entrenado para predecir la clase de paciente desconocido o para encontrar la droga adecuada para el mismo.
