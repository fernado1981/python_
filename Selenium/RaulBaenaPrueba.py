1 Recoger el json que esta en http://demo5977139.mockable.io/qa-cdco/exercises/cars_01, ahi buscar el codigo de suspicious_car, el resto de coches en parking 
meter en una lista de coches sospechosos los que tengan los colores sospechosos
Yo utilice request para hacer el get, que es directo. Y luego mapee en la libreria json standard

import requests
import json

response = requests.get("http://demo5977139.mockable.io/qa-cdco/exercises/cars_01")
data = json.loads(response.text)
suspicious_cars_set = set(data["suspicious_car"])
suspicious_plates = []
for floor in data["parkings"].values():
    for plate in floor:
        if suspicious_cars_set.issubset(set(floor[plate])):
            suspicious_plates.append(plate)
print(suspicious_plates)

2 Buscar en Googla https://www.telefonica.com/es/ y hacer click sobre la primera solucion "valida" 

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.google.com")
element = driver.find_element_by_xpath("//input[@title='Buscar']")
element.send_keys("https://www.telefonica.com/es/\n")
candidate_link = driver.find_elements_by_xpath("//div[@id='search']//div[@class='g']")[0]
candidate_link.find_element_by_xpath(".//a").click()

3 Hacer un listado con todas las tags a cuya href este en el dominio de telefonica 

import re
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.telefonica.com/es/")

list = []
for element in driver.find_elements_by_xpath("//a"):
    href = element.get_attribute("href")
    if href is not None and re.search("https?://.*telefonica\.com/", href):
        list.append(element)


4 Hacer click a la zona de accionistas en https://www.telefonica.com/es/

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.telefonica.com/es/")
# Habia un banner de coockies qsue impedia hacer un click directo
driver.get(driver.find_element_by_xpath("//a[contains(@title,'Zona Accionistas')]").get_attribute("href"))

5 Recolectar la informacion de la cotizacion en la bolsa de NY actual

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.telefonica.com/es/web/zona-accionistas/")
# El componente estaba en otro frame
iframe = driver.find_element_by_id("euroland-ticker-es")
driver.switch_to.frame(iframe)
[element for element in driver.find_elements_by_xpath("//div[@class='TabsContainer']/div") if element.text == 'NYSE'][0].click()
driver.find_element_by_xpath("//div[contains(@class,'Tab_Active')]//span[@class='last']").text
 
