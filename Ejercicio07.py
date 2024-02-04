from color_texto import info, advertencia, texto_es_numero, error, confirm,texto_color

"""
Ejercicio 07

 Calcular la hipotenusa de un triángulo, teniendo como base el valor del cateto 1 y 2 que serán 
dados por el usuario. Para esto debe de hacer uso del Teorema de Pitágoras en el cálculo de la 
hipotenusa teniendo los catetos. (h= √(a^2 )+b^2) no se debe hacer uso de la librería Math.hypot
"""


def calcular_hipotenusa(cateto1, cateto2):
    """
    Metodo para calcular la hipotenusa utilizando el Teorema de Pitágoras
    """
    hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    return hipotenusa


def ingresar_cateto(numero):
    while True:
        valor = input(f"Ingrese el valor del cateto {numero}: ")
        try:
            return float(valor)
        except ValueError:
            print(error("Por favor, ingrese un valor numérico válido."))


def calcular_catetos():
    print(texto_color('Ingrese los valores de los dos catetos para calcular la hipotenusa','magenta'))

    cateto1 = ingresar_cateto('cateto 1')
    cateto2 = ingresar_cateto('cateto 2')

    hipotenusa = calcular_hipotenusa(cateto1, cateto2)

    print(info(f"La hipotenusa del triángulo es: {hipotenusa}"))


if __name__ == "__main__":
    calcular_catetos()
