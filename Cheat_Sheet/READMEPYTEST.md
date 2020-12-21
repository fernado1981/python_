<a name="top"></a>
[Principal](../README.md)<br/>

# PyTest
pytestes un marco que facilita la creación de pruebas simples y escalables. Las pruebas son expresivas y legibles, no se requiere un código estándar. Comience en minutos con una prueba de unidad pequeña o una prueba funcional compleja para su aplicación o biblioteca.

#### Instalar pytest
  
    pip install -U pytest

#### Compruebe que instaló la versión correcta:

    $ pytest --version

#### Cree una función de prueba simple con solo cuatro líneas de código:
*test_sample_fail.py
  
    def func(x):
    return x + 1

    def nombre(name):
    return name

    def test_answer():
    assert func(3) == 5

    def test_nombre():
    assert nombre('Fernando') == 'pepe'
      
**Nota:** esta prueba fallará dado que 3+1 no son 5 y pepe no es igual a 'Fernando'

#### Cree una función de prueba simple con solo cuatro líneas de código:
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

### EJECUCIONES

1. **Ejecutar todas las pruebas**
        
       a) pytest
       b) pytest -ra
       c) python -m pytest
       
2. **Hacer que pare al primer fallo**
  
        Pytest -x
  
3. **hacer que para el n fallo**
 
        Pytest --maxfail=2
    
**NOTA:** En este caso para cuando encuentre el segundo fallo
    
4. **Ejecutar las pruebas de un fichero**
* **sintax:** pytest [path_al_file.py]
    
      pytest pruebas/test_sample_pass.py
     
* **OutPut**<br/>
    =========================== test session starts ============================<br/>
    platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1<br/>
    rootdir: C:\Users\FMANRIQU\Desktop\python<br/>
    collected 2 item                                                            <br/>                                                                                       
    pruebas\test_sample.py .                                             [100%]<br/>
    ============================ 2 passed in 0.03s ============================<br/>

5. **Ejecutar pruebas en un directorio**
* **sintax:** pytest [path_al_directorio]

      pytest pruebas/

* **OutPut**<br/>
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

6. **Ejecutar un test específico de un fichero**
* **sintax:** pytest [path_al_file.py]::[test_a_ejecutar]

      pytest pruebas/test_sample_pass.py::test_nombre

* **OutPut**<br/>
    ====================== test session starts ============================<br/>
    platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1<br/>
    rootdir: C:\Users\FMANRIQU\Desktop\python<br/>
    collected 1 item   <br/>                                                                                                                                                    
    pruebas\test_sample_pass.py .                                    [100%]<br/>
    ========================== 1 passed in 0.02s ==========================<br/>

**Nota:** tambien se podría realizar una ejecución de una fucnion en concreto de una clase:

    pytest test_mod.py::TestClass::test_method
    
7. **Llamar a pytest en código Python**
* **sintax:** pytest.main()
test_sample_pass.py
  
    def func(x):
    return x + 1

    def nombre(name):
    return name

    def test_answer():
    assert func(4) == 5

    def test_nombre():
    assert nombre('Fernando') == 'Fernando'
    
    pytest.main()

* **Output:**<br/>
    ============================= test session starts =============================<br/>
    platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1<br/>
    rootdir: C:\Users\FMANRIQU\Desktop\python\pruebas, configfile: pytest.ini<br/>
    collected 4 items<br/>
    test_sample_fail.py FF                                                   [ 50%]<br/>
    test_sample_pass.py ..                                                   [100%]<br/>
    ================================== FAILURES =============================<br/>
    _________________________________ test_answer _________________________________<br/>

    *def test_answer():<br/>
    *>       assert func(5) == 5<br/>
    *E       assert 6 == 5<br/>
    *E        +  where 6 = func(5)<br/>
    *test_sample_fail.py:11: AssertionError<br/>
    _________________________________ test_nombre _________________________________<br/>

    *def test_nombre():<br/>
    *>       assert nombre('Fernando') == 'fer'<br/>
    *E       AssertionError: assert 'Fernando' == 'fer'<br/>
    *E         - fer<br/>
    *E         + Fernando<br/>
    *test_sample_fail.py:14: AssertionError<br/>
    =========================== short test summary info ========================<br/>
    *FAILED test_sample_fail.py::test_answer - assert 6 == 5<br/>
    *FAILED test_sample_fail.py::test_nombre - AssertionError: assert 'Fernando' =...<br/>
    ========================= 2 failed, 2 passed in 0.42s =========================<br/>

### REPORTE 
## XML
1. **Ejecutar reporte en xml**

        pytest --junitxml=pruebas/report
 
 ## URL
1. **Cree un enlace de URL de registro para cada caso de uso de falla de prueba**
    
        pytest --pastebin=failed
 
2. **Cree un enlace URL para todo el registro de ejecución de la prueba**

        pytest --pastebin=all
 
 ## HTML
 1. **Instalar pytest-html**

        pip install pytest-html
     
 2. **Generar directorio report**
 
![report_directory](../Images/pytest_report.png)
        
 3. **Correr test**

        pytest --html=report.html

**NOTA:** Al ejecutar las pruebas, nos generará un reporte Html como figura abajo, o mejor sería crear un directorio en la raiz que ponga report y dirrigir todos los reports a dicho directorio.

    pytest --html=report/report.html

![report_html](../Images/report_pytest_1.png)
 
      

[Subir](#top)
