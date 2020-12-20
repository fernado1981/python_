1.- Instalacion:
pip3 install behave
pip3 install -U behave

2.- Versión mas reciente desde el repositorio behave:
pip install git+https://github.com/behave/behave

1.- Implementacion de los requistos mínimos:
features/
features/everything.feature
features/steps/
features/steps/steps.py

2.- Creamos un directorio llamado features
mkdir features

3.- Creamos un fichero lamado tutorial.feature:
cd features
touch feature

4.- Implementamos el siguiente ejemplo dentreo del fichero *.feature:
vi tutorial.feature
NOTA: nos pedirá que instalemos el plugin de cucumber

Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!
      
5.- Creamos el directorio steps:
cd  features
mkdir steps

6.- Creamos el fichero tutorial.py:
cd features/steps
touch tutorial.py

7.- Implementamos los steps del feature:
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

8.- Ejecute los escenarios:
behave

9.- Ejecución por nombre de escenario:
sintax: behave -n 'nombre del escenario'
behave -n 'run a simple test'

10.- Ejecute por tag:
Nota: para ello deberemos añadir el tag justo encima del escenario
sintax: behave -t 'nombre del @tag'
behave -t '@slow_tag_name'

11.- Ejecutar sólo un .feature:
sintax: behave -i nombre del .feature
behave -i tutorial.feature

12.- Excluyendo .feature:
Sintax: behave -e file_name
behave -e tutorial.feature


1.- Como funcionan los archivos .feature:

'Dado' que ponemos el sistema en un estado conocido antes de que el usuario (o sistema externo) comience a interactuar con el sistema (en los pasos Cuándo). Evite hablar de la interacción del usuario en situaciones dadas.

'Cuando' nos tomamos acciones clave que el usuario (o sistema externo) lleva a cabo. Esta es la interacción con su sistema que debería (o tal vez no debería) hacer que algún estado cambie.

'Entonces' nos observamos los resultados.