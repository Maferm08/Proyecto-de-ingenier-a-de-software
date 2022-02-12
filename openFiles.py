import codecs
import time
import os

#Iniciar timer para tiempo de ejecución
total_start = time.time()
print("ABRIR ARCHIVOS")
#Path de los archivos que tienen en común
folderpath = r"Files/" 
#Juntar el path en común con el nombre de los archivos y crear lista
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
time_total = 0

"""
en cada html de la lista filepaths se iniciará un timer, se correrá y se terminará el timer
para poder imprimir el tiempo de cada 1 
"""
for path in filepaths:
    start = time.time()
    file = codecs.open(path, "r", "utf-8")
    end = time.time()
    run_time = end - start
    print(path, ': ', run_time)
    time_total = time_total + run_time

# Imprimir tiempos totales de ejecución y de abrir archivos
print("Tiempo total en abrir los archivos: ", time_total)
total_end = time.time()
print("Tiempo total de ejecución: ", total_end - total_start)
    
