import sys


def error():
    print('Você deve passar a nota como argumento do comando')
    print('formato: nota.py <<nota>>')


def error_numeric():
    print('o valor fornecido como argumento deve ser um numero')
    print('formato: nota.py <<nota>>')


def float_check(ehfloat):
    try:
        float(ehfloat)
        return True
    except:
        return False

def calcular_nota(nota):
    if nota > 10:
        print('nota invalida: o valor deve ser entre 0 e 10')
    elif nota == 10:
        print(' voce é o ser supremo do universo')
    elif nota >= 7:
        print('parabens voce passou na média')
    elif nota >= 0:
        print('voce esta de recuperação')
    else:
        print('nota invalida: o valor deve ser entre 0 e 10')



if __name__ == '__main__':
    if len(sys.argv) < 2:
        error()
    #elif not sys.argv[1].isnumeric():
    #    error_numeric()
    elif not float_check(sys.argv[1]):
        error_numeric()
    else:
        calcular_nota(float(sys.argv[1]))
#print(float_check())

    #else:
        # calcular_nota(sys.argv[1])
