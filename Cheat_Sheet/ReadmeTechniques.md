
<a name='top'></a>
[Principal](../README.md)<br/>


*[clasificacion supervisado -> K-Vecinos Más Cercanos (KNN)](#KNN)*<br/>
*[modelo predictivo No supervisado -> Arboles de decisión](#Árboles)*<br/>
*[Regresion -> regresión logística](#RegrasionLogistica)*

<a name='KNN'></a>
## K-Vecinos Más Cercanos (KNN):

En este lab, cargaremos un conjunto de datos de un cliente, adaptaremos la información y utilizaremos el algoritmo de k-vecinos más cercanos para predecir un punto de datos. ¿Qué es K-Vecinos Más Cercano?
Vecinos K Más Cercanos es un algoritmo para aprendizaje supervisado. Donde los datos se entrenana con puntos de datos que corresponden a su clasificación. Como un punto se predice, toma en cuenta los puntos 'K' más cercanos para determinar su clasificación

<KNN.png>

En este caso, tenemos puntos de datos de Clase A y B. Deseamos predecir dónde está la estrella (punto de datos de prueba). Si consideramos un valor k de 3 (3 el punto más cercano) obtendremos una predicción de Clase B. Sin embargo, si consideramos un valor k de 6, obtendremos una predicción de Clase A.

En este sentido, es importante considerar el valor de k. Mirando al diagrama, deberías deducir lo que es realmente un algormitmo de K Vecinos más cercanos. Tiene en cuenta los vecinos 'K' más cercano (puntos) cuando predice la clasificación de los puntos de prueba.

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
Imagina un proveedor de telecomunicaciones que ha segmentado la base de sus clientes por servicio, categorizando a los clientes en cuatro grupos. Si los datos demográficos se pueden usar para predecir la pertenencia de grupo del envío, la compañía podría personalizar las ofertas para los prospectos. Es un problema de clasificación. O sea, dado un set de datos, con etiquetas predefinidas, necesitaremos construir un modelo para predecir la clase de un nuevo o desconocido caso.

Este ejemplo hace foco en datos demográficos, sean region, edad, estado civil, para predecir patrones de uso.

El campo objetivo (target), llamado custcat, tiene cuatro valores posibles que corresponden a los cuatro grupos de clientes, a saber: 1- Servicio Básico 2- E-Servicio 3- Servicio Plus 4- Servicio Total

Nuestro objetivo es construir un clasificador para predecir la clase de casos desconocidos. Utilizaremos un tipo específico de clasificación llamado K vecino más cercano.

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
Definir feature sets, x:

     df.columns

### conversion de data fame de panda a Numpy array:
    X = df[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] .values  #.astype(float)
    X[0:5]
    
    y = df['custcat'].values
    y[0:5]
    
### normalizar datos:
La estandarización de Datos brinda a los datos cero media y varianza de unidad, es buena práctica, especialmente para algoritmos tales como KNN el cual se basa en distancia de casos:

    X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
    X[0:5]

### Train Test Split:
Al margen de la exactitud de la muestra, está el porcentaje de las predicciones correctas que el modelo hace de los datos para el que no ha sido entrenado. Al hacer un entrenamiento y prueba en el mismo set de datos, de seguro tendrán baja exactitud de muestra debido a la probabilidad de estar sobre dimensionado.

Es importante que nuestros modelos tengan una exactitud de muestra alta porque el propósito de cualquier modelos es lograr predicciones lo más certeras posibles sobre datos no conocidos. Entonces, ¿cómo podemos mejorar la precisión? Una forma es utilizar un enfoque de evaluación llamado Train/Test Split (Entrenar/Evaluar Dividir).
Esta forma requiere dividir el set de datos en conjuntos de entrenamiento y prueba, los cuales son mutuamente exclusivos. Luego de ello, se entrena con el conjunto de entrenamiento y se prueba con el conjunto de prueba.

Este método brinda una evaluación más precisa porque el set de prueba no es parte del conjunto de datos que ha sido utilizado para entrenar los datos. Es más realista para los problemas actuales.

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
    print ('Set de Entrenamiento:', X_train.shape,  y_train.shape)
    print ('Set de Prueba:', X_test.shape,  y_test.shape)
    
### Clasificación:
K-vecinos más cercano (K-NN)
Importar librería
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
En clasificación multietiqueta, la función classification accuracy score computa la certeza del subconjunto. Esta función es igual a la función jaccard_similarity_score. Básicamente, calcula cómo se relacionan las etiquetas actuales con las etiquetas predichas dentro del set de pruebas.
    
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

<a name='Árboles'></a>
## ÁRBOLES DE DECISIÓN:
En este ejercicio, aprenderás un algoritmo muy popular de machine learning llamado Árboles de Decisión. Utilizarás un algoritmo de clasificación para construir un modelo basado en datos históricos de pacientes y sus respectivos medicamentos. Luego, utilizarás el árbol de decisión recién entrenado para predecir la clase de paciente desconocido o para encontrar la droga adecuada para el mismo.

### Importando librerías:
    import numpy as np 
    import pandas as pd
    from sklearn.tree import DecisionTreeClassifier
    
### Acerca del set de datos:
Imagina que eres un investigador médico recolectando datos para un estudio. Has colectado datos de un grupo de pacientes, todos sufrieron la misma enfermedad. Durante su tratamiento, cada paciente respondio a una de 5 medicaciones, Droga A, Droga B, Droga c, Droga x e y.

Parte de tu trabajo es construir un modelo para encontrar la droga apropiada para un próximo paciente con la misma enfermedad. El conjunto de características son Edad, Sexo, Presión Sanguínea y Colesterol. El objetivo es la droga ante la cual cada paciente respondió.

Este es un ejemplo de un clasificador binario donde puedes utilizar un set de entrenamiento del set de datos para construir un árbol de decisión para predecir la clase de pacientes desconocidos o para prescribirle a un nuevo paciente.

### Descargando los Datos:
    !wget -O drug200.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/drug200.csv
    
### lee los datos utilizando el marco de datos de panda:
    my_data = pd.read_csv("drug200.csv", delimiter=",")
    my_data[0:5]
    
### ver el tamaño de los datos:
    my_data.describe()
    
### Pre-procesamiento:
Utilizando my_data como los datos de panda el archivo Drug.csv, declara las siguientes variables:

X as the Feature Matrix (datos de my_data)
<li> <b> y </b> como el <b> vector de respuesta (target) </b> </li>

### Elimina la columna que contiene el target ya que no posee valores numéricos.
    X = my_data[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
    X[0:5]
    
Como te puedes imaginar, algunas características son de categoría, tales como Sex o__BP__. Desafortunadamente, los árboles de Decisión Sklearn no manejan variables categóricas. Pero las podemos convertir en valores numéricos. pandas.get_dummies() Convertir variable categórica en indicadores de variables.

    from sklearn import preprocessing
    le_sex = preprocessing.LabelEncoder()
    le_sex.fit(['F','M'])
    X[:,1] = le_sex.transform(X[:,1]) 

    le_BP = preprocessing.LabelEncoder()
    le_BP.fit([ 'LOW', 'NORMAL', 'HIGH'])
    X[:,2] = le_BP.transform(X[:,2])

    le_Chol = preprocessing.LabelEncoder()
    le_Chol.fit([ 'NORMAL', 'HIGH'])
    X[:,3] = le_Chol.transform(X[:,3]) 

    X[0:5]
 
### completar la variable objetivo (target):
    y = my_data["Drug"]
    y[0:5]
   
### Configurando el Arbol de Decisión:
Estaremos utilizando entrenar/probar separar en nuestro árbol de decisión. Importemos train_test_split de sklearn.cross_validation.
    
    from sklearn.model_selection import train_test_split
    
Ahora train_test_split devolverá 4 parámetros diferentes. Los nombraremos:
X_trainset, X_testset, y_trainset, y_testset

El train_test_split necesitará los parámetros:
X, y, test_size=0.3, and random_state=3.

La X e y son los arreglos necesarios ántes de la operación dividir/separar, test_size representa el grado del dataset de pruebas, y el random_state asegura que obtendremos las mismas divisiones.

    X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)
    
### Modelando:
Primero crearemos una instancia del DecisionTreeClassifier llamada drugTree.
Dentro del clasificador, especificaremos criterion="entropy" para que podamos ver la nueva información de cada nodo.

    drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
    drugTree # muestra los parámetros por omisión
    
Luego, adaptaremos los datos con la matriz de entrenamiento X_trainset y el vector de respuesta y_trainset
    
    drugTree.fit(X_trainset,y_trainset)

### Predicción:
Ahora hagamos algunas predicciones en el dataset de pruebas y guardémoslas en una variable llamada predTree.
    
    predTree = drugTree.predict(X_testset)
   
Puedes imprimir predTree y y_testset si quieres comparar visualmente la predicción con los valores actuales.

    print (predTree [0:5])
    print (y_testset [0:5])
 
 ### Evaluación:
 importemos metrics de sklearn y revisemos la precisión de nuestro modelo.

    from sklearn import metrics
    import matplotlib.pyplot as plt
    print("Precisión de los Arboles de Decisión: ", metrics.accuracy_score(y_testset, predTree))
    
Accuracy classification score calcula la precisión del subconjunto: las etiquetas predichas para una muestra deben coincidir con las correspondientes etiquetas en y_true.

En la clasificación multietiqueta, la función devuelve un subconjunto de precisión. Si el conjunto de etiquetas predichas para una muestra coincide totalmente con el conjunto de etiquetas, entonces la precisión del subconjunto es 1.0; de no ser así, es 0.0.

### Visualización:
    from sklearn.externals.six import StringIO
    import pydotplus
    import matplotlib.image as mpimg
    from sklearn import tree
    %matplotlib inline 

    dot_data = StringIO()
    filename = "drugtree.png"
    featureNames = my_data.columns[0:5]
    targetNames = my_data["Drug"].unique().tolist()
    out=tree.export_graphviz(drugTree,feature_names=featureNames, out_file=dot_data, class_names= np.unique(y_trainset), filled=True,              special_characters=True,rotate=False)  
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_png(filename)
    img = mpimg.imread(filename)
    plt.figure(figsize=(100, 200))
    plt.imshow(img,interpolation='nearest')
    
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
