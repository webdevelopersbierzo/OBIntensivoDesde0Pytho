# Enunciado: Utilizando la API de https://openweathermap.org/ y realizando una petición a
# https://api.openweathermap.org/data/2.5/weather?q={city%20name}&appid={API%20key}
# obtén la temperatura máxima y mínima, para la# ciudad que proporcione el usuario.

import json
import requests
import datetime

apikey = '4f2125592feeff61ab305993c3b60215'


def solicitar_datos(ciudad):
    r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={apikey}')
    resultado = json.loads(r.text)
    temperatura = resultado["main"]
    return temperatura


def conv_kelvin_celsius(temp):
    return round((temp - 273), 1)


def temperatura_actual(data):
    datos = data
    temp_actual = datos["temp"]
    return conv_kelvin_celsius(temp_actual)


def temperatura_maxima(data):
    temp_maxima = data["temp_max"]
    return conv_kelvin_celsius(temp_maxima)


def temperatura_minima(data):
    temp_minima = data["temp_min"]
    return conv_kelvin_celsius(temp_minima)


def main():
    now = datetime.datetime.now()
    # Salida
    print(f'Introduce el nombre de una ciudad')
    ciudad = input()
    tem_actu = solicitar_datos(ciudad)
    print(f'Datos de {ciudad}\t\t{now.hour}:{now.minute} de {now.day}/{now.month}/{now.year}')
    print(f'---------------------')
    print(f'la temperatura es:{temperatura_actual(tem_actu)} C')
    print(f'Minima: {temperatura_minima(tem_actu)} C')
    print(f'maxima: {temperatura_maxima(tem_actu)} C')


main()


if __name__ == '__main':
    main()