
def searchlist(list, elemento):
    for i in range(len(list)):
        if i == elemento:
            return True
        else:
            return False


def numerosprimos(numero):

    numero = int(numero)
    primos = []

    for x in range(1, numero):
        condicion = 0
        while condicion < 3 and x <= 2 and x <= numero:
            if x == 1:
                x += 1
                continue
            if x == 2:
                if x % 1 == 0:
                    condicion += 1
                    if x % x == 0:
                        primos.append(x)
                        x += 1
                        condicion += 1
        if x > 2:
            for x in range(x, numero + 1):
                if x % 1 == 0:  # si es divisible entre 1
                    if x % primos[0] != 0:  # si no es divisible entre 2
                        if x == 3:
                            primos.append(x)
                        if x < 24 and x % primos[1] != 0:  # si no es divisible entre 3
                            primos.append(x)
                        elif x >= 24 and x % primos[1] != 0:  # si no es divisible entre 3
                            buscarenlist = searchlist(primos, x)  # buscar en lista x
                            if not buscarenlist:  # si no esta en la lista
                                contador = 0
                                for i in primos:    # para cada elemento en la lista
                                    contador += 1
                                    resultado = x % i == 0  # divido el numero por el elemento
                                    if resultado:
                                        contador = 0
                                        break
                                    if resultado == False and contador == len(primos):
                                        primos.append(x)

                        else:
                            continue
                    elif x % primos[0] == 0:
                        continue
            else:
                print(primos)
                size = len(primos)
                return print(f'\tLos numeros primos entre 1 y {numero} son {size}')

print(f'Introduce un numero:')
numero = input()
while not numero.isnumeric():
    print(f'Introduce un numero:')
    numero = input()
numerosprimos(numero)

