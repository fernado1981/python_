# Diccionarios url:<br/>
  Marca={"url":"http://www.marca.es"}<br/>
  ElMundo={"url":"http://www.elmundo.es}<br/>
  Periodico={"Marca":Marca,"ElMundo":ElMundo}<br/>
  
# Api:<br/>
  response = requests.get(url)<br/>
  print(response.status_code)<br/>
  repsonse=response.json()<br/>
  lista.append(response)<br/>

# Pirmera solución valida en browser:<br/>
  driver.find_elements_by_xpath("//div["id='search']//div[@class='g']")[0]<br/>
  driver.find_element_by_xpath(".//a").click()<br/>

# Obtener los href del directorio<br/>
  for a in driver.find_element_by_xpath(".//a"):<br/>
    print(a.getattribute('href'))<br/>

# Click Zona accionistas:<br/>
  driver.find_element_by_link_text("Accionistas e inversores").click()<br/>

# Recolectar info bolsa NY:<br/>
  iframe = driver.find_element_by_id("id del frame")<br/>
  driver.switch_to.frame(iframe)<br/>
  driver.find_element.by_link_text('NYSE').click()<br/>

  for valor in driver.find_elelemts_by_css_selector(.Tab_Active .last):<br/>
    print(valot.text)<br/>

