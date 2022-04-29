
import os
import time

#Iniciamos timer de ejecución
total_start = time.time()
#Path de los archivos que tienen en común
folderpath = r"Sort_text_files/" 
#Juntar el path en común con el nombre de los archivos y crear lista
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

time_total = 0
word_bank = ['Gauch', 'elephants', 'CSCE', 'Arkansas', 'gift', 'abcdef', '20','20.07', 
             '123-456-7890', 'lawyer', 'consumers', 'garden' 'computer', 'United' 'States', 'laws']

dic =[]

for path in filepaths:
    #Inicia temporizador
    start = time.time()
    # Abrimos html que queremos
    try:
        file = open(path, "r").read()
    except:
        # En caso de tener algún valor del alfabeto latino
        file = open(path, encoding="Latin-1").read()
    
    # Fill dic with every word in 049, hard, medium and simple
    file = file.split()
    for word in word_bank:
        if word in file:
            if path not in dic:
                dic.append(path)

search_tokens=[]
i = 0
for value in dic:
    search_tokens.append(str(i+1)+ ": " + value)
    i = i + 1


search_tokens_file = open("Activity_12_files/search_tokens.html", "w")
search_tokens_file.write('\n'.join(search_tokens))
#Terminamos timer 
end = time.time()
run_time = end - start
# Imprimir tiempos totales de ejecución y de abrir archivos
print("Tiempo total de búsqueda: ", run_time)
total_end = time.time()
print("Tiempo total de ejecución: ", total_end - total_start)
