from color_texto import info, advertencia, texto_es_numero, error, confirm, texto_color

"""
Ejercicio 13

Desarrollar un algoritmo que reciba como entrada un carácter y de cómo salida el número de 
ocurrencias de dicho carácter en una cadena de caracteres.
"""


def contar_ocurrencias(caracter, cadena):
    """
    Utilizar el método count para contar las ocurrencias del carácter en la cadena
    """
    return cadena.count(caracter)


def ingresar_caracter():
    while True:
        valor = input("Ingrese un carácter: ")
        if len(valor) == 1:
            return valor
        else:
            print(info("Por favor, ingrese solo un carácter."))


def ingresar_cadena():
    return input("Ingrese una cadena de caracteres: ")


def calcular_caracter():
    print(texto_color('Ingrese un carácter y una cadena para contar sus ocurrencias en la cadena', 'magenta'))

    caracter = ingresar_caracter()
    cadena = ingresar_cadena()

    ocurrencias = contar_ocurrencias(caracter, cadena)

    print(info(f"El carácter '{caracter}' aparece {ocurrencias} veces en la cadena."))


if __name__ == "__main__":
    calcular_caracter()
