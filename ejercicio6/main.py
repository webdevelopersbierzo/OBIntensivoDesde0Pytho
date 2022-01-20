import sys
from getpass import getpass

letra = {'a': '00', 'b': '01', 'c': '02', 'd': '03', 'e': '04', 'f': '05', 'g': '06', 'h': '07', 'i': '08', 'j': '09',
         'k': '10', 'l': '11', 'm': '12', 'n': '13', 'o': '14', 'p': '15', 'q': '16', 'r': '17', 's': 18, 't': '19',
         'u': '20', 'v': '21', 'w': '22', 'x': '23', 'y': '24', 'z': '25'}


def pass_convert(passwd):
    passwmin = passwd.lower()
    list = []

    for i in range(len(passwmin)):
        letter = passwmin[i]
        for x in letra:
            if letter == ' ':
                list.insert(i, '26')
                break
            elif letter == x:
                list.insert(i, letra[x])
                break
            else:
                continue

    print(list)

def app():
    passwd = ''
    try:
        passwd = getpass(stream=sys.stderr)

    except Exception as err:
        print('Error: ', err)
    else:
        print('Has introducido la contraseña')
    pass_convert(passwd)


if __name__ == '__main__':
    app()
