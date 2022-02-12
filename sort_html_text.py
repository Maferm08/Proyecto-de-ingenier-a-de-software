import re
import os
import time


#Iniciamos timer de ejecución
total_start = time.time()
#Path de los archivos que tienen en común
folderpath = r"Remove_tags_files/" 
#Juntar el path en común con el nombre de los archivos y crear lista
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

time_total = 0


"""
For que recorre todos los archivos html en Remove_tags_files y crea en la carpeta Sort_text_files los mismos htmls pero 
organizando su texto alfabeticamente 
"""

for path in filepaths:
    #Inicia temporizador
    start = time.time()
    # Abrimos html que queremos
    try:
        file = open(path, "r").read()
    except:
        # En caso de tener algún valor del alfabeto latino
        file = open(path, encoding="Latin-1").read()
    file = re.sub('[^a-zA-Z]+ ', '', file)
    li = list(file.split(" "))
    # Creamos html con el mismo nombre en la carpeta Sort_text-files
    sort_text_file = open("Sort_text_files/" + path.replace("Remove_tags_files/", ""), 'w')
    # Escribimos en el nuevo html el mismo html de carpeta File pero eliminando todos los espacios vacíos y los
    res = []
    for string in li:
        if string != '':
            res.append(string)
    res = sorted(res)
    sort_text_file.write('\n'.join(res))
    sort_text_file.close()

    #Terminamos timer
    end = time.time()
    run_time = end - start
    print(path.replace("Remove_tags_files/", ""), ': ', run_time)
    time_total = time_total + run_time

# Imprimir tiempos totales de ejecución y de abrir archivos
print("Tiempo total en organizar el html: ", time_total)
total_end = time.time()
print("Tiempo total de ejecución: ", total_end - total_start)


