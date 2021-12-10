# fuente: https://www.youtube.com/watch?v=O7o1iyhuA9o
# https://www.youtube.com/watch?v=o8s9z6icgPY

from selenium import webdriver
#from csv import reader
import time

from csv import DictReader

# crear archivo para los resultados
f = open ('resultado01.csv','w')
f.write("Nombre,Casos\n")

# descargar driver de Chrome de https://chromedriver.chromium.org/
driver = webdriver.Chrome('D:/Oscar/Datos Incorruptibles/scrapdatosinc/chromedriver.exe')
# web que vamos a scrapear
driver.get("https://appbp.contraloria.gob.pe/BuscadorCGR/Informes/Inicio.html")

# espera 3 segundos mientras carga el navegador y abre la web
time.sleep(5)

# iterate over each line as a ordered dictionary and print only few column by column name
with open('comite_2020.csv', 'r', encoding="utf8") as read_obj:
	csv_dict_reader = DictReader(read_obj)
	for row in csv_dict_reader:
		#print(row['Nombre'])
		nombre = row['Nombre']

		
		# datain será la caja de texto del buscador
		datain = driver.find_element_by_xpath('//*[@id="inpGeneral"]')

		datain.clear()

		# escribir en la caja de texto
		datain.send_keys(nombre)

		# Click en el botón "Buscar"
		driver.find_element_by_xpath('//*[@id="btnBuscar"]').click()
		time.sleep(1)

		casos = driver.find_element_by_xpath('//*[@id="lbltotalItems"]')

		partes_strcasos = casos.text.split()

		print(nombre+","+partes_strcasos[1])
		f.write(nombre+","+partes_strcasos[1]+"\n")

f.close()
driver.quit()