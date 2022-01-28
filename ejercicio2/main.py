# Enunciado: Crea una agenda de teléfonos que se gestione por consola, que te permita:
# 1) Añadir a cualquier persona, indicando nombre y después teléfono
# 2) Buscar el teléfono de una persona
# Objetivo:
# - Aprender a manejar la entrada y la salida por consola.
# - El uso de colecciones (array o diccionario)
#Ampliacion
# - Al buscar a una persona, que te muestre todas aquellas que comiencen por el texto que has introducido. Ejemplo:
#    Introduce un nombre: Pep
#    Resultados:
#    - Pepe 659331013
# - Pepe Martín 633743551
import os

import imprimirmenu as imenu

agenda = {}


def pedirnombre():
    '''
    Funcion que pide un nombre y telefono y lo guarda en un lita
    :return:
    '''
    print('Introduce el nombre: ')
    nombre = input()
    print('Introduce el telefono. ')
    telefono = input()
    agenda[nombre] = telefono


def buscarcontacto():
    '''
    buscar un contacto con el nombre entero
    :return:
    '''

    borrarPantalla()
    imenu.imprimehead()
    print('Introduce el contacto a buscar: ')
    searchcont = input()

    if searchcont in agenda:
        resultado = agenda[searchcont]
        borrarPantalla()
        imenu.imprimehead()
        print('El telefono es: ', resultado,'\t')
        print('Menu Principal [0]')
        volver = input()

        if volver == '0':
            app()
        else:
            borrarPantalla()
            print('Introduce la opcion correcta')
            buscarcontacto()

    else:
        borrarPantalla()
        imenu.imprimehead()
        error = 'Contacto no encontrado'
        print(error)
        print('Menu Principal [0]')
        volver = input()
        if volver == 0:
            app()


def buscarporletras():
    # imprimimos menu
    borrarPantalla()
    imenu.imprimehead()
    print('Introduce el contacto a buscar')
    #pedimos datos
    searchcont = input()
    listacaracter = list(searchcont)#guardamos un una lista con el metodo list
    if not listacaracter:
        print('¡¡¡¡¡Introduce un nombre')
        buscarporletras()
    else:
        for key in agenda:
            if key.startswith(listacaracter[0]):
                print(key)
            if key.startswith(listacaracter[0] + listacaracter[1]):
                print(key)
            if key.startswith(listacaracter[0] + listacaracter[2]):
                print(key)
            else:
                print('no hay coincidencias')


def borrarPantalla():
    if os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')
    else:
        os.system ('clear')


def app(menu='1'):
    borrarPantalla()
    menu = menu
    salir = False
    while not salir:

        if menu == '1' and menu.isalnum():
            borrarPantalla()
            imenu.imprimehead()
            imenu.imprimemain()
            imenu.imprimefoot()

            opcion = input()
            if opcion == '1' :
                borrarPantalla()
                imenu.imprimehead()
                pedirnombre(),

                print('Deseas continuar: ')
                opc = input()
                app()
                if opc == 'y':
                    salir = False

                elif opc == 'n':
                    salir = True

            elif opcion == '2' :
                borrarPantalla()
                app('2')

            elif opcion == '3':
                exit()
            else:
                print('Introduce la opcion correcta')
        elif menu == '2' and menu.isalnum():
            imenu.imprimehead()
            imenu.imprimebuscar()
            imenu.imprimefoot()
            opc2 = input()
            if opc2 == '1' and opc2.isalnum():
                buscarcontacto()
                app('2')

            elif opc2 == '2'and opc2.isalnum():
                buscarporletras()
                app('2')
            elif opc2 == '3' and opc2.isalnum():
                app()
            else:
                print('elige la opcion')
                app('2')
        else:
            print('Elige la opcion correcta')
            app('2')

if __name__ == "__main__":
    app()
