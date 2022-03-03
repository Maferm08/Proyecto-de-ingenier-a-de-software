from itertools import count
import re
import os
import time

#Iniciamos timer de ejecución
total_start = time.time()
#Juntar el path en común con el nombre de los archivos y crear lista
filepaths  = ['Sort_text_files/049.html', 'Sort_text_files/simple.html', 'Sort_text_files/medium.html', 'Sort_text_files/hard.html']
time_total = 0

"""
For que recorre todos los archivos html y crea en la carpeta Remove_tags_files los mismos htmls pero sin tags
"""
total_count = dict()
for path in filepaths:
    #Inicia temporizador
    start = time.time()
    # Abrimos html que queremos
    try:
        file = open(path, "r").read()
    except:
        # En caso de tener algún valor del alfabeto latino
        file = open(path, encoding="Latin-1").read()
    
    counts = dict()
    words = file.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

        if word in total_count:
            total_count[word] += 1
        else:
            total_count[word] = 1
    sort_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    Sort_alphabetical_files = open( "Sort_Frequency_files/"+path.replace("Sort_text_files/", ""), 'w')
    for i in sort_counts:
        Sort_alphabetical_files.write(str(i)+'\n')
    Sort_alphabetical_files.close() 
    
    #Terminamos timer
    end = time.time()
    run_time = end - start
    print(path.replace("Remove_tags_files/", ""), ': ', run_time)
    time_total = time_total + run_time

sort_total_counts = sorted(total_count.items(), key=lambda x: x[1], reverse=True)
for i in sort_total_counts:
    print(i)
# Imprimir tiempos totales de ejecución y de abrir archivos
print("Tiempo total en eliminar las etiquetas: ", time_total)
total_end = time.time()
print("Tiempo total de ejecución: ", total_end - total_start)


