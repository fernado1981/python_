# PyTest
pytestes un marco que facilita la creación de pruebas simples y escalables. Las pruebas son expresivas y legibles, no se requiere un código estándar. Comience en minutos con una prueba de unidad pequeña o una prueba funcional compleja para su aplicación o biblioteca.

**Instalar pytest**
  
    pip install -U pytest

**Compruebe que instaló la versión correcta:**

    $ pytest --version

**Crea tu primera prueba**
**Cree una función de prueba simple con solo cuatro líneas de código:**
test_sample_fail.py
  
    def func(x):
      return x + 1
      
    def test_answer():
      assert func(3) == 5
      
**Nota:** esta prueba fallara dado que 3+1 no son 5

**Cree una función de prueba simple con solo cuatro líneas de código:**
test_sample_pass.py
  
    def func(x):
      return x + 1
      
    def test_answer():
      assert func(4) == 5
  
**Nota:** esta prueba pasara dado que 4+1 no son 5

**Ejecutar las pruebas de un fichero**
    
     $ pytest test_sample.py
     
**Ejecutar todas las pruebas**

    $ pytest
