from color_texto import info, advertencia, error, confirm, texto_color, texto_es_numero

"""
Ejercicio 05 y Ejercicio 8

En este problema Se ingresa un valor numérico de 8 dígitos que representa una fecha con el 
siguiente formato: aaaammdd. Esto es: los 4 primeros dígitos representan el año, los siguientes 2 
dígitos representan el mes y los 2 dígitos restantes representan el día. Se pide informar por 
separado el día, el mes y el año de la fecha ingresada. Para su solución se debe de hacer uso de 
divisiones, operador modulo y conversión de double a entero.

ingresa un valor numérico de 8 dígitos que representa una fecha con el siguiente
formato: aaaammdd verificar si la fecha es correcta en sentido de numero de
meses y días.

"""


def obtener_dia_mes_ano(fecha):
    if verificar_fecha(fecha):
        fecha_entero = int(fecha)
        ano = fecha_entero // 10000
        mes = (fecha_entero // 100) % 100
        dia = fecha_entero % 100
        return dia, mes, ano
    else:
        print(error('Formato de fecha incorrecto. Ingrese una fecha válida.'))
        return None, None, None


def verificar_fecha(fecha):
    """
    Método para verificar si la longitud de la fecha es 8 dígitos y si es un número
    """
    return len(fecha) == 8 and texto_es_numero(fecha)


def obtener_fecha():
    """
    Método para obtener por separado el día, el mes y el año de la fecha ingresada.
    """
    print('')
    print(texto_color('Mostrar la fechacon formato de año,mes,dia', 'magenta'))

    print(info('Ingrese una fecha con el formato aaaammdd: '))
    fecha = input()

    dia, mes, ano = obtener_dia_mes_ano(fecha)

    if dia is not None:
        print(info(f'Año:{ano},Mes:{mes},Dia:{dia}'))


if __name__ == '__main__':
    obtener_fecha()
