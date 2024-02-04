from color_texto import info, advertencia, texto_es_numero, error, confirm,texto_color

"""
Ejercicio 09
Se debe de ingresar un numero comprendido entre 1 y 12 por el usuario. El algoritmo debe 
de imprimir el mes correspondiente en texto.
"""


def obtener_nombre_mes(numero_mes):
    """
    Metodo para definirun diccionario con la correspondencia entre números y nombres de meses
    """
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    # Verificar si el número de mes está en el rango válido
    if 1 <= numero_mes <= 12:
        return meses[numero_mes]
    else:
        return "Número invalido. Ingrese un número entre 1 y 12."


def ingresar_numero_mes():
    while True:
        valor = input("Ingrese un número entre 1 y 12: ")
        try:
            numero_mes = int(valor)
            return numero_mes
        except ValueError:
            print(error("Ingrese un valor numérico válido."))


def mes():
    print(texto_color('Ingrese un número de mes para obtener el nombre correspondiente','magenta'))

    numero_mes = ingresar_numero_mes()

    nombre_mes = obtener_nombre_mes(numero_mes)

    print(info(f"El mes correspondiente al número {numero_mes} es: {nombre_mes}"))


if __name__ == "__main__":
    mes()
