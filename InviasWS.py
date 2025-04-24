from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

def obtener_elementos(origenes_destinos):
    # Inicializar el navegador Edge
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)

    # Cargar la página
    driver.get("https://hermes2.invias.gov.co/SIV/")

    # Configurar el tiempo de espera
    wait = WebDriverWait(driver, 20)

    # Lista para guardar los resultados
    resultados = []

    try:
        # Ciclo para origen y destino
        for origen, destino in origenes_destinos:
            # Refresca la página para evitar dobles búsquedas
            driver.refresh()
            # Espera a que carguen los resultados
            time.sleep(5)

            try:
                # Escribe el origen
                wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Buscar dirección"]')))
                input_origen = driver.find_elements(By.XPATH, '//input[@placeholder="Buscar dirección"]')[0]
                input_origen.clear()
                input_origen.send_keys(origen)

                # Espera a que carguen los resultados
                time.sleep(5)
                input_origen.send_keys(Keys.ENTER)

                # Espera a que carguen los resultados
                time.sleep(5)

                # Escribe el destino
                input_destino = driver.find_elements(By.XPATH, '//input[@placeholder="Buscar dirección"]')[1]
                input_destino.clear()
                input_destino.send_keys(destino)

                # Espera a que carguen los resultados
                time.sleep(5)
                input_destino.send_keys(Keys.ENTER)

                print(f"Origen y destino seleccionados: {origen} → {destino}")

                # Espera a que carguen los resultados
                time.sleep(5)

                # Obtiene la distancia
                xpath_distancia = '//div[@class="esri-directions__other-costs-total"]'
                wait.until(EC.presence_of_element_located((By.XPATH, xpath_distancia)))
                distancia_texto = driver.find_element(By.XPATH, xpath_distancia).text

                # Limpia y convierte la distancia
                distancia_limpia = distancia_texto.replace(" km", "").replace(",", ".")
                distancia = float(distancia_limpia)
                
                # Obtiene el tiempo
                xpath_tiempo = '//div[@class="esri-directions__costs-value"]'
                wait.until(EC.presence_of_element_located((By.XPATH, xpath_tiempo)))
                tiempo_texto = driver.find_element(By.XPATH, xpath_tiempo).text

                # Limpia y convierte el tiempo
                tiempo_limpio = tiempo_texto.lower().replace(" h", "").replace(" min", "").split()
                horas = int(tiempo_limpio[0]) if len(tiempo_limpio) > 0 else 0
                minutos = int(tiempo_limpio[1]) if len(tiempo_limpio) > 1 else 0
                tiempo = round(horas + minutos / 60, 2)

                # Obtiene el costo del peaje por categoría 1
                xpath_categoria_1 = '//table[@class="categorias"]/tbody/tr[td[text()="Categoría 1"]]/td[2]'
                costo_peaje_elemento = wait.until(EC.presence_of_element_located((By.XPATH, xpath_categoria_1)))
                costo_texto = costo_peaje_elemento.text

                # Limpia y convierte el costo del peaje
                costo_limpio = costo_texto.replace("$", "").replace("\xa0", "").replace(".", "").strip()
                costo_peaje_categoria_1 = int(costo_limpio) if costo_limpio else 0

                # Creamos el diccionario con la información
                resultado = {
                    "origen": origen,
                    "destino": destino,
                    "tiempo": tiempo,
                    "distancia": distancia,
                    "costo_peaje": costo_peaje_categoria_1
                }

                print(f"Información obtenida: {resultado}")

                # Agrega la información al diccionario de resultados de la búsqueda
                resultados.append(resultado)

            # Excepción para evitar interrumpir el ciclo
            except Exception as e:
                print(f"Error al procesar ruta {origen} → {destino}: {e}")
                resultados.append({
                    "origen": origen,
                    "destino": destino,
                    "tiempo": 0,
                    "distancia": 0,
                    "costo_peaje": 0,
                    "error": str(e)
                })

                # Refresca la página para evitar dobles búsquedas
                driver.refresh()

                # Espera a que carguen los resultados
                time.sleep(3)

    finally:
        driver.quit()

    return resultados