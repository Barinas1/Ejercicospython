from color_texto import info, advertencia, texto_es_numero, error, confirm,texto_color

"""
Ejercicio 12

Se debe de ingresar un numero por el usuario, este debe de ser evaluado para verificar que el 
número de cifras sea par y verificar si el número es capicúa o no.
"""


def es_numero_par(numero):
    """
    Metodo para verificar si el numero es par
    """
    return len(str(numero)) % 2 == 0


def es_capicua(numero):

    cadena_numero = str(numero)

    return cadena_numero == cadena_numero[::-1]


def ingresar_numero():
    while True:
        valor = input("Ingrese un número: ")
        try:
            numero = int(valor)
            return numero
        except ValueError:
            print(error("Por favor, ingrese un valor numérico válido."))


def calcular_numero():
    print(texto_color('Ingrese un número para verificar si el número de cifras es par y si es capicúa','magenta'))

    numero = ingresar_numero()

    if es_numero_par(numero):
        print(info("El número de cifras es par."))
    else:
        print(info("El número de cifras no es par."))

    if es_capicua(numero):
        print(info("El número es capicúa."))
    else:
        print(info("El número no es capicúa."))


if __name__ == "__main__":
    calcular_numero()
