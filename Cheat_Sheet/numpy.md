
[Principal](../README.md)<br/>
[Api_Post](READMEPOST.md) | [Api_Get](READMEGET.md)  | [Tuplas](READMETupleSet.md) | [Listas](READMELIST.md) | [Diccionarios](READMEDIC.md) | [Selenium](../Selenium/README.md)

Documentación: <https://numpy.org/doc/>

# Numpy
Es una biblioteca para crear vectores y matrices grandes multidimensionales, junto con una gran colección de funciones matemáticas de alto nivel para operar con ellas.

### Instalar Jupiter, matploitlib
- pip3 install jupyter 
- pip3 install matplotlib
- python3 -mpip install -U matplotlib
- python3 -mpip install -U matplotlib

### Importar numpy:
    import numpy as np

### Convertir una lista a un arreglo numpy:
    a=np.array([1,2,3,4,5])
    
### type(), obtiene el tipo <numpy.ndarray>:
    print("El tipo es: ", type(a))
    
### dtype, obtener el tipo de datos del arreglo:
    print("los datos son de tipo: ", a.dtype)
    
### mean(), obtener la media del arreglo:
    mean_a = a.mean()
    print("la media de los datos del arreglo es:", mean_a)
  
## CREAR y TRAZAR FUNCIONES:
### Importar librería:
    import matplotlib.pyplot as plt
    
### crear un vector con cuatro puntos equidistanciados, desde 0 hasta 2:
    np.linspace(0, 2, 4)

### crear la funcion y=sin(x)+2 , uando la matriz numpy x
    x = np.linspace(0.2 * np.pi, 100)
    y = np.sin(x)
    
### matplotlib.pylot, Trazar la solucion:
    plt.plot(x, y)
    plt.show()
