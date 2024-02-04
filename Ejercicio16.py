from color_texto import info, advertencia, texto_es_numero, error, confirm, texto_color

"""
Ejercicio 16

 Desarrollar un algoritmo que solicite una frase de mínimo 5 palabras y capitalizar la cadena.
"""


def capitalizar_frase(frase):
    """
    Metodo para dividir la frase en palabras
    """
    palabras = frase.split()

    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]

    frase_capitalizada = ' '.join(palabras_capitalizadas)

    return frase_capitalizada


def ingresar_frase():
    while True:
        frase = input("Ingrese una frase con mínimo 5 palabras: ")

        if len(frase.split()) >= 5:
            return frase
        else:
            print(info("La frase debe contener al menos 5 palabras."))


def cadena_capitalizar():
    print(texto_color('Ingrese una frase con mínimo 5 palabras para capitalizarla', 'magenta'))

    frase = ingresar_frase()

    frase_capitalizada = capitalizar_frase(frase)

    print(info("Frase capitalizada:"))
    print(frase_capitalizada)


if __name__ == "__main__":
    cadena_capitalizar()
