import re
import os
import time

#Iniciamos timer de ejecución
total_start = time.time()
#Path de los archivos que tienen en común
folderpath = r"Files/" 
#Juntar el path en común con el nombre de los archivos y crear lista
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

time_total = 0
#Todos los signos que va a buscar y eliminar 
CLEANR = re.compile('<.*?>') 

"""
For que recorre todos los archivos html y crea en la carpeta Remove_tags_files los mismos htmls pero sin tags
"""
for path in filepaths:
    #Inicia temporizador
    print(path)
    start = time.time()
    # Abrimos html que queremos
    try:
        file = open(path, "r").read()
    except:
        # En caso de tener algún valor del alfabeto latino
        file = open(path, encoding="Latin-1").read()
    # Creamos html con el mismo nombre en la carpeta Remove_tags_files
    remove_html_tags_file = open("Remove_tags_files/" + path.replace("Files/", ""), 'w')
    # Escribimos en el nuevo html el mismo html de carpeta File pero substracting los valores de la variable CLEANR
    remove_html_tags_file.write(re.sub(CLEANR, '', file))
    remove_html_tags_file.close()
    #Terminamos timer
    end = time.time()
    run_time = end - start
    # print(path, ': ', run_time)
    time_total = time_total + run_time
    print("time_total", time_total)

# Imprimir tiempos totales de ejecución y de abrir archivos
print("Tiempo total en eliminar las etiquetas: ", time_total)
total_end = time.time()
print("Tiempo total de ejecución: ", total_end - total_start)


