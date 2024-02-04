from color_texto import info, advertencia, texto_es_numero, error, confirm,texto_color

"""
Ejercicio 14 

Desarrollar un algoritmo que determine si una cadena de caracteres es palíndroma. Una 
cadena se dice palíndromo si al invertirla es igual a ella misma.
"""


def es_palindromo(cadena):
    """
    Eliminar espacios y convertir a minúsculas para hacer la comparación sin
    ser sensible a mayúsculas y minúsculas
    """
    cadena = cadena.replace(" ", "").lower()
    """
    Comparar la cadena original con su versión invertida
    """

    return cadena == cadena[::-1]


def ingresar_cadena():
    return input("Ingrese una cadena de caracteres: ")


def verificar_cadena():
    print(texto_color('Ingrese una cadena para determinar si es un palíndromo','magenta'))

    cadena = ingresar_cadena()

    if es_palindromo(cadena):
        print(info("La cadena es un palíndromo."))
    else:
        print(info("La cadena no es un palíndromo."))


if __name__ == "__main__":
    verificar_cadena()
