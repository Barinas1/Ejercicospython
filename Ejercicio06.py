from color_texto import info, advertencia, texto_es_numero, error, confirm,texto_color

"""
Ejercicio 06

 Leer tres valores numéricos enteros, indicar cuál es el mayor, cuál es el del medio y cuál, el 
menor. Considerar que los tres valores serán diferentes.
"""


def encontrar_mayor_medio_menor(num1, num2, num3):
    """
    Metodo para encontrar el numero mayor,medio y menor
    """
    mayor = max(num1, num2, num3)

    menor = min(num1, num2, num3)

    medio = (num1 + num2 + num3) - mayor - menor

    return mayor, medio, menor


def es_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False


def ingresar_valor(posicion):
    while True:
        valor = input(f"Ingrese el valor {posicion}: ")
        if es_entero(valor):
            return int(valor)
        else:
            print(error("Por favor, ingrese un valor entero válido."))


def verificar_numero():
    print(texto_color('Ingrese tres numeros diferentes','magenta'))

    numero_1 = ingresar_valor("numero 1")
    numero_2 = ingresar_valor("numero 2")
    numero_3 = ingresar_valor("numero 3")

    mayor, medio, menor = encontrar_mayor_medio_menor(numero_1, numero_2, numero_3)

    print(info(f"El numero mayor es: {mayor}"))
    print(info(f"El numero del medio es: {medio}"))
    print(info(f"El numero menor es: {menor}"))


if __name__ == "__main__":
    verificar_numero()
