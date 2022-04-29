from Activity12 import filepaths, word_bank
import json
import os
import time

start = time.time()
word_list = []
for word in word_bank:
    word_list.append("Retrieve " + word)
    word_list.append("Top documents")
    i = 0
    for path in filepaths:
        #Inicia temporizador
        # Abrimos html que queremos
        try:
            file = open(path, "r").read()
        except:
            # En caso de tener algún valor del alfabeto latino
            file = open(path, encoding="Latin-1").read()
        
        file = file.split()
        if word in file:
            if i < 10:
                word_list.append(str(i+1) + ". " + path.replace("Sort_text_files/", ""))
                i = i + 1
    
    word_list.append("")
end= time.time()
search_tokens_file = open("Activity_13_files/top_10_search_documents.html", "w")
search_tokens_file.write('\n'.join(word_list))

# Imprimir tiempos totales de ejecución y de abrir archivos
print("Tiempo total de búsqueda: ", end - start)
total_end = time.time()
print("Tiempo total de ejecución: ", total_end - start)