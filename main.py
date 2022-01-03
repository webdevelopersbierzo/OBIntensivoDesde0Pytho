
import os.path

# Guardamos el resultado de os.listdir en una variable que es una lista de string

ruta = "/Users/oscarcorralgarcia/Downloads"
directorios = os.listdir(ruta)

############################################
# Imprimimos todos los archivos y directorios
############################################

print('------ Directorios y archivos-------')

for file in directorios:
    print(file)
    
print('------------------------------------')
print('')

############################################
# Imprimiendo ficheros solamente del directorio descargas
############################################

print('--------Imprimiendo ficheros--------')

# recorremos la lista y comprobamos que no sea un directorio
for file in directorios:
    # Buscamos los que son directorios o archivos
    # si isdir es true
    ruta2 = ruta + '/' + file
    isdir = os.path.isdir(ruta2)
    if not isdir:
        print()
        print(ruta2)
