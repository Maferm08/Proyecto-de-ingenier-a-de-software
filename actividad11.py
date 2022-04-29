import re
import os
import time
from sort_frequency_posting import activity_11_posting
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
documents={}
documents_list=[]
i = 0
for path in filepaths:
    #Inicia temporizador de Documents
    start_document_time = time.time()
    documents[i+1]=path.replace("Files/", "")
    documents_list.append(str(i+1) + ": " + path.replace("Files/", ""))
    i = i + 1

    documents_file = open("Activity_11_files/Documents.html",'w')
    documents_file.write('\n'.join(documents_list))
end_document_time = time.time()

#Inicia temporizador de Posting
start_posting_time = time.time()
token_string = "Tokenized/Tokenized"
posting_updated = []
for token in activity_11_posting:
    check = token.replace(token_string,"")
    for key, value in documents.items():
        if value in check:
            posting_updated.append(str(key) + ": " + token.replace(token_string + value + " ,",""))
    

posting_file = open("Activity_11_files/posting.html", "w")
posting_file.write('\n'.join(posting_updated))
end_posting_time = time.time()
print("Tiempo para crear Documents.html: ", end_document_time - start_document_time)
print("Tiempo para crear Posting.html: ", end_posting_time - start_posting_time)
total_end = time.time()
print("Tiempo total", total_end - total_start)
