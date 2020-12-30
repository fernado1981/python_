<a name='top'></a>
[Principal](../README.md)<br/>

# BEHAVE_CUCUMBER:
## Documentación:

**FUNCIONAMIENTO ARCHIVOS .feature:**
- 'Given' que ponemos el sistema en un estado conocido antes de que el usuario (o sistema externo) comience a interactuar con el sistema (en los pasos Cuándo). Evite hablar de la interacción del usuario en situaciones dadas.
- 'When' nos tomamos acciones clave que el usuario (o sistema externo) lleva a cabo. Esta es la interacción con su sistema que debería (o tal vez no debería) hacer que algún estado cambie.
- 'Then' nos observamos los resultados.

## EJEMPLO:
#### 1.- Implementamos el siguiente ejemplo dentro del fichero *.feature:
    vi tutorial.feature
**NOTA:** nos pedirá que instalemos el plugin de cucumber

    Feature: showing off behave

    Scenario: run a simple test
     Given we have behave installed
     When we implement a test
     Then behave will test it for us!
      
#### 2.- Creamos el directorio steps:
    cd features
    mkdir steps

#### 3.- Creamos el fichero tutorial.py:
    cd features/steps
    touch tutorial.py

#### 4.- Implementamos los steps del feature:
    vi tutorial.py

      from behave import *

      @given('we have behave installed')
      def step_impl(context):
        pass

      @when('we implement a test')
      def step_impl(context):
        assert True is not False

      @then('behave will test it for us!')
      def step_impl(context):
        assert context.failed is False

## EJECUCIÓN:
#### 1.- Ejecute los escenarios con report:
    behave -f html -o reports/report.html

#### 2.- Ejecute los escenarios con allure reports:
    behave -f allure_behave.formatter:AllureFormatter -o reports/allure/results ./features
    allure serve reports/allure/results

#### 3.- Ejecute los escenarios:
    behave
    
#### 4.- Ejecución por nombre de escenario:
**sintax:** behave -n 'nombre del escenario'
   
    behave -n 'run a simple test'

#### 5.- Ejecute por tag:
**Nota:** para ello deberemos añadir el tag justo encima del escenario
**sintax:** behave -t 'nombre del @tag'

    behave -t '@slow_tag_name'

#### 6.- Ejecutar sólo un .feature:
**sintax:** behave -i nombre del .feature

    behave -i tutorial.feature

#### 7.- Excluyendo .feature:
**Sintax:** behave -e file_name

    behave -e tutorial.feature
   
#### 8.- Help:
    behave -help

[Subir](#top)
