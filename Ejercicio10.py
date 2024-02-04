from color_texto import info, advertencia, texto_es_numero, error, confirm,texto_color

"""
Ejercicio 10

 Dado un número (leído por teclado), que representa los segundos que ha invertido una 
persona en hacer un examen, determinar cuántas horas, minutos y segundos ha invertido. 
Imprima el resultado por pantalla.
"""


def convertir_segundos_a_horas_minutos_segundos(total_segundos):
    # Calcular las horas
    horas = total_segundos // 3600

    # Calcular los minutos
    minutos = (total_segundos % 3600) // 60

    # Calcular los segundos restantes
    segundos = total_segundos % 60

    return horas, minutos, segundos


def ingresar_total_segundos():
    while True:
        valor = input("Ingrese el número total de segundos: ")
        try:
            total_segundos = int(valor)
            return total_segundos
        except ValueError:
            print(error("Por favor, ingrese un valor numérico válido."))


def tiempo():
    print(texto_color('Ingrese el número total de segundos para convertir a horas, minutos y segundos','magenta'))

    total_segundos = ingresar_total_segundos()

    horas, minutos, segundos = convertir_segundos_a_horas_minutos_segundos(total_segundos)

    print(info(f"Tiempo invertido: {horas} horas, {minutos} minutos y {segundos} segundos"))


if __name__ == "__main__":
    tiempo()
