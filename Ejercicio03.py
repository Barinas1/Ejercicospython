import math

from color_texto import info, advertencia, texto_es_numero, error,texto_color

"""
Ejercicio 02

 En este problema debemos de definir una constante con el valor de PI como 3,1416 y 
tenemos un único dato de entrada dado por el usuario: un valor numérico que puede ser entero o 
flotante que indicara el radio de un círculo. La salida del algoritmo será el área del circulo teniendo 
en cuenta que A=PI*r^2. Si el usuario ingresó valor negativo o cero tendremos que emitir un 
mensaje informando las causas por las cuales no se podrá efectuar la operación.
"""


def calcular_area_circulo():
    """
    Método para calcular el área de un círculo.
    """
    print('')
    print(texto_color('Calcular el área de círculo','magenta'))

    print(info('Ingrese el radio del círculo: '))
    radio = texto_es_numero(input())

    if radio is not None and radio > 0:
        area = math.pi * radio ** 2
        print(info(f'El área del círculo con radio {radio} es: {round(area, 2)}'))
    else:
        print(error('No se puede calcular el área.'))


if __name__ == '__main__':
    calcular_area_circulo()
