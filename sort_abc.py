import re
import os
import time
from typing import List

#Iniciamos timer de ejecución
total_start = time.time()
#Path de los archivos que tienen en común
folderpath = r"Sort_text_files/" 
#Juntar el path en común con el nombre de los archivos y crear lista
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

time_total = 0
#Todos los signos que va a buscar y eliminar 
CLEANR = re.compile('<.*?>') 

"""
For que recorre todos los archivos html y crea en la carpeta Remove_tags_files los mismos htmls pero sin tags
"""
consolidated_string=" "
 
for path in filepaths:
    #Inicia temporizador
    start = time.time()
    # Abrimos html que queremos
    try:
        file = open(path, "r").read()
    except:
        # En caso de tener algún valor del alfabeto latino
        file = open(path, encoding="Latin-1").read()
    
    
    Sort_alphabetical_files = open( "sort_alphabetical/"+path.replace("Sort_text_files/", ""), 'a')

    file_sorted_alphabetically="\n ".join(sorted(file.lower().split()))
    
    
    Sort_alphabetical_files.write(file_sorted_alphabetically)
    consolidated_string+= file_sorted_alphabetically
    
    Sort_alphabetical_files.close()
    
    #Terminamos timer
    end = time.time()
    run_time = end - start
    print(path.replace("Files/", ""), ': ', run_time)
    time_total = time_total + run_time

# Imprimir tiempos totales de ejecución y de abrir archivos
consolidated_file=open('actividad_4_consolidado.txt','w') 
consolidated_file.write("\n ".join(sorted(consolidated_string.split())))
consolidated_file.close()
print("Tiempo total en eliminar las etiquetas: ", time_total)
total_end = time.time()
print("Tiempo total de ejecución: ", total_end - total_start)


