from color_texto import info, advertencia, error, confirm, texto_color

"""
Ejercicio 15
 
Pedir un número de 0 a 99 y mostrarlo escrito. Por ejemplo, para 56 mostrar: cincuenta y 
seis
"""


def numero_a_palabras(numero):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    especiales_10_19 = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho",
                        "diecinueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    if 0 <= numero <= 99:
        if numero < 10:
            return unidades[numero]
        elif numero < 20:
            return especiales_10_19[numero - 10]
        else:
            """
            Metodo para dividir el número en dígito de las decenas y unidades
            """
            decena = numero // 10
            unidad = numero % 10
            palabras = decenas[decena]

            if unidad > 0:
                palabras += f" y {unidades[unidad]}"

            return palabras
    else:
        return "Número fuera del rango permitido (0-99)."


def ingresar_numero():
    while True:
        valor = input("Ingrese un número entre 0 y 99: ")
        try:
            numero = int(valor)
            return numero
        except ValueError:
            print(error("Por favor, ingrese un valor numérico válido."))


def numero_en_palabra():
    print(texto_color('Ingrese un número entre 0 y 99 para mostrarlo en palabras', 'magenta'))

    numero = ingresar_numero()

    palabras = numero_a_palabras(numero)

    print(info(f"Representación en palabras: {palabras}"))


if __name__ == "__main__":
    numero_en_palabra()
