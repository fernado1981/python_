# Diccionarios url:
  Marca={"url":"http://www.marca.es"}
  ElMundo={"url":"http://www.elmundo.es}
  Periodico={"Marca":Marca,"ElMundo":ElMundo}
  
# Api:
  response = requests.get(url)
  print(response.status_code)
  repsonse=response.json()
  lista.append(response)

#Pirmera solución valida en browser:
  driver.find_elements_by_xpath("//div["id='search']//div[@class='g']")[0]
  driver.find_element_by_xpath(".//a").click()

#Obtener los href del directorio
  for a in driver.find_element_by_xpath(".//a"):
    print(a.getattribute('href'))

#Click Zona accionistas:
  driver.find_element_by_link_text("Accionistas e inversores").click()

#Recolectar info bolsa NY:
  iframe = driver.find_element_by_id("id del frame")
  driver.switch_to.frame(iframe)
  driver.find_element.by_link_text('NYSE').click()

  for valor in driver.find_elelemts_by_css_selector(.Tab_Active .last):
    print(valot.text)

