from color_texto import info, texto_es_numero, error,texto_color

"""
Ejercicio 02

En este problema tenemos un único dato de entrada: un valor numérico entero
que deberá ingresar el usuario. La salida del algoritmo será informar si el usuario
ingresó un valor par o impar. Sabemos que un número par es aquel que es
divisible por 2 o, también, que un número es par si el valor residual que se obtiene
al dividirlo por 2 es cero. Según lo anterior, podremos informar que el número
ingresado por el usuario es par si al dividirlo por 2 obtenemos un resto igual a
cero. De lo contrario, informaremos que el número es impar.
"""


def verificar_par_o_impar(numero):
    """
    Metodo para verificar si el numero es divisible por 2
    """
    if numero % 2 == 0:
        return "El número ingresado es par."
    else:
        return "El número ingresado es impar."


def ingresar_numero():
    while True:
        print(info("Ingrese un número: "))
        valor = input()
        if texto_es_numero(valor):
            return float(valor)
        else:
            print(error("Por favor, ingrese un valor numérico válido."))


def par_impar():
    print(texto_color("Ingrese un número para validar si es par o impar",'magenta'))
    numero = ingresar_numero()
    resultado = verificar_par_o_impar(numero)
    print(info(resultado))


if __name__ == "__main__":
    par_impar()
