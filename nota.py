import sys


def error():
    print('Voc^deve passar a nota como argumento do comendo')
    print('formato: nota.py <<nota>>')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        error()
    #else:
        # calcular_nota(sys.argv[1])
