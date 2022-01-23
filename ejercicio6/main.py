
import sys
from getpass import getpass
from random import randrange

letra = {'a': '00', 'b': '01', 'c': '02', 'd': '03', 'e': '04', 'f': '05', 'g': '06', 'h': '07', 'i': '08', 'j': '09',
         'k': '10', 'l': '11', 'm': '12', 'n': '13', 'o': '14', 'p': '15', 'q': '16', 'r': '17', 's': '18', 't': '19',
         'u': '20', 'v': '21', 'w': '22', 'x': '23', 'y': '24', 'z': '25'}

intercambio = [['b', 'e', 'h', 'k'], ['c', 'f', 'i', 'l'], ['d', 'g', 'j', 'm']]


def pass_convert(passwd=None):
    passwmin = passwd.lower()
    lista = []
    num_one = 0
    num_two = 0
    sumatotal = 0
    valor1 = ''
    valor2 = ''

    for i in range(len(passwmin)):
        letter = passwmin[i]
        for x in letra:
            if letter == ' ':  # si hay un espacio le añadimos 26
                lista.insert(i, '26')
                break
            elif letter == x:
                lista.insert(i, letra[x])
                break
            else:
                continue

    # imprimos la codificacion inicial de la password
    print(f'codificacion inicial \n{lista}')

    # calculando la suma total de la lista
    for j in range(0, len(lista)):
        sumatotal = sumatotal + int(lista[j])

    # añadiendo comprobaciones
    listlen = len(lista)  # tamaño de lista

    # Rellenando hasta 12 elementos la lista
    if 6 <= listlen <= 12:
        for i in range(listlen, 12):
            numbers = randrange(30, 99, 2)
            lista.insert(i+1, numbers)
    print(f'rellenando hasta 12 con numeros aleatorios\n {lista}')
    # Añadiendo la suma total de la lista
    lista.insert(13, sumatotal)
    print(f'Añadido el total de la suma\n{lista}')

    # Intercambiando posiciones de la lista y añadiendo a la lista
    for z in range(0, 3, 1):

        if z == 0:
            # Generando posiciones aleatorias
            posx = randrange(0, 2, 1)
            posy = randrange(0, 4, 1)

            num_one = letra.get(intercambio[posx][posy])
            lista.insert(14, num_one)  # añadimos la primera posición a cambiar a la lis
            valor1 = lista[int(num_one)]  # guardamos el valor de la lista correspondiente
            continue

        elif z == 1:
            # Generando posiciones aleatorias
            posx = randrange(0, 2, 1)
            posy = randrange(0, 4, 1)

            num_two = letra.get(intercambio[posx][posy])
            lista.insert(15, num_two)  # añadimos la segunda posición a cambiar a la lista
            valor2 = lista[int(num_two)]  # guardamos el valor de la lista correspondiente

            continue

        else:
            print(f'Antes del intercambion de numeros\n{lista}')
            lista.insert(16, randrange(10, 99, 1))  # insertando un numero aleatorio al final
            #  Intercambiamos las posiciones
            lista[int(num_one)] = valor2
            lista[int(num_two)] = valor1
            print(f'intercambiando numeros\n{lista}')
            continue
    print(f'Resultado de la codificacion\n{lista}')
    resultado = ''.join(map(str, lista))

    return resultado


def app():
    passwd = ''
    try:
        passwd = getpass(stream=sys.stderr)
        while len(passwd) <= 5:
            print(f'Introduce una contraseña entre 6 y 12 caracteres')
            passwd = getpass(stream=sys.stderr)

    except Exception as err:
        print('Error: ', err)
    else:
        print('Has introducido la contraseña')
    print(f'La clave decodificada es : ')
    print(f'{pass_convert(passwd)}')


if __name__ == '__main__':
    app()
