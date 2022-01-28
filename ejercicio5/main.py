# @Course: Intensivo desde 0
# @Ejercicio: Ejercicio5
# @author: Oscar Corral Garcia
# Convierte un Excel a CSV

import pandas as pd

file = 'MOCK_DATA.xlsx'
file2 = 'MOCK_DATA.csv'

dataframe = pd.read_excel(file)



# Abrimos el fichero
f = open(file2, 'a+')

#Escribimos la primera fila

f.write("nombre,email\n")
# leemos el dataframe
i = 0
while i < dataframe.size/2:
    listadt = dataframe.iloc[i]
    for j in range(len(listadt)):
        dato = listadt[j]
        #escribimos el dato en el fichero
        if j == 0:
            f.write(dato)
            f.write(",")
        else:
            f.write(dato)
            f.write("\n")
    i += 1


# Cerramos el fichero
f.close()

#leemos el fichero csv
f = open('MOCK_DATA.csv')
datos = None
while datos !="":
    datos = f.readline()
    print(datos)
f.close()