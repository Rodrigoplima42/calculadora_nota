import sys


def error():
    print('Você deve passar a nota como argumento do comendo')
    print('formato: nota.py <<nota>>')


def error_numeric():
    print('o valor fornecido como argumento deve ser um numero')
    print('formato: nota.py <<nota>>')



if __name__ == '__main__':
    if len(sys.argv) < 2:
        error()
    elif not sys.argv[1].isnumeric():
        error_numeric()
print(sys.argv[1].isnumeric())

    #else:
        # calcular_nota(sys.argv[1])
