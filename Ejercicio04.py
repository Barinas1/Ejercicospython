from color_texto import info, advertencia, texto_es_numero, error,confirm,texto_color

"""
Ejercicio 04
 En este problema tenemos un único dato de entrada: un valor numérico entero que deberá 
ingresar el usuario. La salida del algoritmo será informar si el numero ingresado por el usuario es 
múltiplo de 2 y 3. Sabemos que un número es múltiplo de otro cuando al dividir estos dos 
números el residuo sea 0. Si el usuario ingresó un valor negativo o cero tendremos que emitir un 
mensaje informando las causas por las cuales no se podrá efectuar la operación.

"""


def verificar_multiplo_2_y_3():
    """
    Método para verificar si un número  es múltiplo de 2 y 3.
    """
    print('')
    print(texto_color('Verificar el múltiplo de 2 y 3','magenta'))

    print(info('Ingrese un número: '))
    numero = texto_es_numero(input())

    if numero is not None and numero >= 0:
        es_multiplo_de_2 = numero % 2 == 0
        es_multiplo_de_3 = numero % 3 == 0

        if es_multiplo_de_2 and es_multiplo_de_3:
            print(confirm(f'{numero} es múltiplo de 2 y 3.'))
        else:
            print(error(f'{numero} no es múltiplo de 2 y 3.'))
    else:
        print(error('No se puede verificar.ingrese otro numero'))


if __name__ == '__main__':
    verificar_multiplo_2_y_3()
