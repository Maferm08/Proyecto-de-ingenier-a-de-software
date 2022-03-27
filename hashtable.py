from itertools import count
import re
import os
import time

from dict_hash import dict_hash
from random import randint
#Iniciamos timer de ejecución
total_start = time.time()
#Juntar el path en común con el nombre de los archivos y crear lista
filepaths  = ['Tokenized/Tokenized049.html', 'Tokenized/Tokenizedhard.html', 'Tokenized/Tokenizedmedium.html', 'Tokenized/Tokenizedsimple.html']
time_total = 0

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
    for word in file:
        val = word.rpartition(',')[0] # word, 1
        if val not in dic:
            dic.append(val)

# FILL POSTING
#ordenar alfabeticamente dic
dic=sorted(dic, key=lambda x:x.lower())

# crear diccionario postin
posting=[]
# abrir los html's para poder leerlos 
file049 = open(filepaths[0], "r").read()
fileHard = open(filepaths[1], "r").read()
fileMedium = open(filepaths[2], "r").read()
fileSimple = open(filepaths[3], "r").read()
hash_dic_posting=dict()
# for que recorre todo dic para buscar la palabra con su frequencia dentro de cada html
for x in dic:
    if x in file049:
        freq = x.rpartition(',')[2]
        hash_dic_posting[hash(filepaths[0])]=filepaths[0] + ' , ' + freq
        posting.append(filepaths[0] + ' , ' + freq)
    if x in fileHard:
        freq = x.rpartition(',')[2]
        hash_dic_posting[hash(filepaths[1])]=filepaths[1] + ' , ' + freq
        posting.append(filepaths[1] + ' , ' + freq)
    if x in fileMedium:
        freq = x.rpartition(',')[2]
        hash_dic_posting[hash(filepaths[2])]=filepaths[2] + ' , ' + freq
        posting.append(filepaths[2] + ' , ' + freq)
    if x in fileSimple:
        freq = x.rpartition(',')[2]
        hash_dic_posting[hash(filepaths[3])]=filepaths[3] + ' , ' + freq
        posting.append(filepaths[3] + ' , ' + freq)
        
sorted_hash_dic_posting=[]
for key, value in hash_dic_posting.items():
    sorted_hash_dic_posting.append(str(key)+': '+value)
    


# Create posting.html
posting_files = open( "Activity_8_files/posting.html", 'w')
posting_files.write('\n'.join(sorted_hash_dic_posting))
posting_files.close()

# DICCIONARIO
# crear diccionario que guarde en cuántos docs se repite la palabra
frequency_of_docs = {}


# buscar en dic cada palabra y si se repite aumentar su frecuencia 
for word in dic:
    val = word.rpartition(',')[0] # word, 1
    freq = 1
    if val not in frequency_of_docs:
        freq = freq + 1
    frequency_of_docs[val] = freq


# Agregar posting a diccionario 
diccionario = []
hash_dic=dict()
posting = 0
for word in frequency_of_docs:
    hash_dic[hash(word)]=(word + ',' + str(frequency_of_docs[word]) + ',' + str(posting))
    diccionario.append(word + ',' + str(frequency_of_docs[word]) + ',' + str(posting))
    posting= frequency_of_docs[word] + posting
sorted_hash_dic=[]
for key, value in hash_dic.items():
    sorted_hash_dic.append(str(key)+': '+value)
# print(hash_dic)
posting_files = open( "Activity_8_files/diccionario.html", 'w')
posting_files.write('\n'.join(sorted_hash_dic))
posting_files.close()


# Imprimir tiempos totales de ejecución y de abrir archivos
print("Tiempo total en organizar el html: ", time_total)
total_end = time.time()
print("Tiempo total de ejecución: ", total_end - total_start)