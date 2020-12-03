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

    def nombre(name):
    return name

    def test_answer():
    assert func(3) == 5

    def test_nombre():
    assert nombre('Fernando') == 'pepe'
      
**Nota:** esta prueba fallará dado que 3+1 no son 5 y pepe no es igual a 'Fernando'

**Cree una función de prueba simple con solo cuatro líneas de código:**
test_sample_pass.py
  
    def func(x):
    return x + 1

    def nombre(name):
    return name

    def test_answer():
    assert func(4) == 5

    def test_nombre():
    assert nombre('Fernando') == 'Fernando'
  
**Nota:** esta prueba pasará dado que 4+1 no son 5 y 'Fernando' es igual a 'Fernando'

**Ejecutar las pruebas de un fichero**
* sintax: pytest [path_al_file.py]
    
      pytest pruebas/test_sample_pass.py
     
=========================== test session starts ============================<br/>
platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1<br/>
rootdir: C:\Users\FMANRIQU\Desktop\python<br/>
collected 2 item                                                            <br/>                                                                                       
pruebas\test_sample.py .                                             [100%]<br/>
============================ 2 passed in 0.03s ============================<br/>
     
**Ejecutar todas las pruebas**

    pytest

**Ejecutar pruebas en un directorio**
* sintax: pytest [path_al_directorio]

      pytest pruebas/
    
====================== test session starts ==========================<br/>
platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1<br/>
rootdir: C:\Users\FMANRIQU\Desktop\python<br/>
collected 4 items <br/>                                                                                                                                                 
pruebas\test_sample_fail.py FF                               [ 50%]<br/>
pruebas\test_sample_pass.py ..                               [100%]<br/>
============================ FAILURES ==========================<br/>
____________________________ test_answer ___________________________<br/>

*def test_answer():<br/>
*>   assert func(3) == 5<br/>
*E   assert 4 == 5<br/>
*E    +  where 4 = func(3)<br/>
*pruebas\test_sample_fail.py:8: AssertionError<br/>
____________________________ test_nombre ____________________________<br/>

*def test_nombre():<br/>
*>    assert nombre('Fernando') == 'Pepe'<br/>
*E    AssertionError: assert 'Fernando' == 'Pepe'<br/>
*E     - Pepe<br/>
*E         + Fernando<br/>
*pruebas\test_sample_fail.py:11: AssertionError<br/>
====================== short test summary info ==========================<br/>
*FAILED pruebas/test_sample_fail.py::test_answer - assert 4 == 5<br/>
*FAILED pruebas/test_sample_fail.py::test_nombre - AssertionError: assert 'Fernando' == 'Pepe'<br/>
====================== 2 failed, 2 passed in 0.10s =========================<br/>

**Ejecutar un test específico de un fichero**
* sintax: pytest [path_al_file.py]::[test_a_ejecutar]
    
      pytest pruebas/test_sample_pass.py::test_nombre

====================== test session starts ============================<br/>
platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1<br/>
rootdir: C:\Users\FMANRIQU\Desktop\python<br/>
collected 1 item   <br/>                                                                                                                                                    
pruebas\test_sample_pass.py .                                    [100%]<br/>
========================== 1 passed in 0.02s ==========================<br/>


