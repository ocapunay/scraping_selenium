from selenium import webdriver
import time

nombre = "escribe aquí un nombre de prueba"
# descargar driver de Chrome de https://chromedriver.chromium.org/
driver = webdriver.Chrome('D:/Oscar/Datos Incorruptibles/scrapdatosinc/chromedriver.exe')

# web que vamos a scrapear
driver.get("https://appbp.contraloria.gob.pe/BuscadorCGR/Informes/Inicio.html")

# espera 5 segundos mientras carga el navegador y abre la web
time.sleep(5)

# datain será la caja de texto del buscador
datain = driver.find_element_by_xpath('//*[@id="inpGeneral"]')
# escribir en la caja de texto
datain.send_keys(nombre)

# Click en el botón "Buscar"
driver.find_element_by_xpath('//*[@id="btnBuscar"]').click()

casos = driver.find_element_by_xpath('//*[@id="lbltotalItems"]')

partes_strcasos = casos.text.split()

print(nombre+","+partes_strcasos[1]+"\n")

driver.quit()
