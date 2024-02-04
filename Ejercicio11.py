from color_texto import info, advertencia, texto_es_numero, error, confirm,texto_color

"""
Ejercicio 11

Dado un número entero leído por pantalla, muestre cada uno de los dígitos del número en 
orden inverso. Ej: Si el número es 324, se debe mostrar 4, 2, 3.
"""


def mostrar_digitos_en_orden_inverso(numero):
    cadena_numero = str(numero)

    for digito in reversed(cadena_numero):
        print(digito)


def ingresar_numero():
    while True:
        valor = input("Ingrese un número entero: ")
        try:
            numero = int(valor)
            return numero
        except ValueError:
            print(error("Por favor, ingrese un valor numérico válido."))


def numero_inverso():
    print(texto_color('Ingrese un número entero para mostrar sus dígitos en orden inverso','magenta'))

    numero = ingresar_numero()

    print(info("Dígitos en orden inverso:"))
    mostrar_digitos_en_orden_inverso(numero)


if __name__ == "__main__":
    numero_inverso()
