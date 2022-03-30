from unittest import result
from hashtable import *

dic = dict()

posting_files = open("Activity_10_files/diccionario.html", 'w')

for key, value in hash_dic.items():

    listOfInts = value.split(",")
    try:
        numRepeticiones = int(listOfInts[1])
        numTokens = int(listOfInts[2])
        resultado = 0 if numTokens == 0 else numRepeticiones * 100 / numTokens
        dic[key] = resultado
    except:
        print("Se presento una excepcion")

nuevoArr = []

for key, value in dic.items():
    nuevoArr.append((str(key) + ": " + str(resultado)))

posting_files.write('\n'.join(nuevoArr))

posting_files.close()

