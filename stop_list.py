from sort_frequency_posting import frequency_of_docs
import time

#Iniciamos timer de ejecución
total_start = time.time()
time_total = 0

try:
    file = open('Activity_9_files\stop_list.html', "r").read()
except:
    # En caso de tener algún valor del alfabeto latino
    file = open('Activity_9_files\stop_list.html', encoding="Latin-1").read()
    
# Fill dic with every word in stop list
file = file.split()
sorted_hash_dic=[]
# Recorre arreglo con palabra y frecuencia revisando que si cumple con los requisitos se agregue a sorted_hash_dic
"""
Requisitos
1. Que la palabra no se encuentre en file = Activity9/stop_list.html
2. Que la frecuencia de repeticiones de la palabra sea mayor a 1
3. Que el tamaño de la palabra sea mayor a 1 letra
"""
for key, value in frequency_of_docs.items():
    if key not in file and int(value) > 1 and len(key) > 1:
        sorted_hash_dic.append(str(key)+': ' + str(value))


# Create diccionario.html
posting_files = open( "Activity_9_files/diccionario.html", 'w')
posting_files.write('\n'.join(sorted_hash_dic))
posting_files.close()
 

# Imprimir tiempos totales de ejecución y de abrir archivos
total_end = time.time()
print("Tiempo total de ejecución: ", total_end - total_start)