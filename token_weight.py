from unittest import result
from hashtable import *

dic = dict()

posting_files = open("Activity_10_files/diccionario.html", 'w')

for key, value in hash_dic.items():

    listOfInts = value.split(",")
    print("listOfInts: " + listOfInts)
    numRepeticiones = int(listOfInts[1])
    numTokens = int(listOfInts[2])
    resultado = 0 if numTokens == 0 else numRepeticiones * 100 / numTokens
    dic[key] = resultado
    posting_files.write('\n'.join(str(key) + ": " + str(resultado)))

posting_files.close()
