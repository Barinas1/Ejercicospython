def texto_color(texto: str, color: str) -> str:
    """
    Metodo para darle color a un texto

    :arg
    texto(str):Texto al que se le va a dar color.
    color(str):Color que se le va a dar color.

    :return
    texto(str):El texto con el color dado
    """
    global ascii__color, ascii_color
    ascii_colo = "\033[39m{}\033[00m"
    if color == "negro":
        ascii_color = "\033[30m{}\033[00m"
    if color == "rojo_oscuro":
        ascii_color = "\033[31m{}\033[00m"
    if color == "verde_oscuro":
        ascii_color = "\033[32m{}\033[00m"
    if color == "amarillo_oscuro":
        ascii_color = "\033[33m{}\033[00m"
    if color == "azul_oscuro":
        ascii_color = "\033[34m{}\033[00m"
    if color == "magenta_oscuro":
        ascii_color = "\033[35m{}\033[00m"
    if color == "cyan_oscuro":
        ascii_color = "\033[36m{}\033[00m"
    if color == "gris":
        ascii_color = "\033[37m{}\033[00m"
    if color == "gris_oscuro":
        ascii_color = "\033[90m{}\033[00m"
    if color == "rojo":
        ascii_color = "\033[91m{}\033[00m"
    elif color == "verde":
        ascii_color = "\033[92m{}\033[00m"
    elif color == "amarillo":
        ascii_color = "\033[93m{}\033[00m"
    elif color == "azul":
        ascii_color = "\033[94m{}\033[00m"
    elif color == "magenta":
        ascii_color = "\033[95m{}\033[00m"
    elif color == "cyan":
        ascii_color = "\033[96m{}\033[00m"
    elif color == "blanco":
        ascii_color = "\033[97m{}\033[00m"

    return ascii_color.format(texto)


def error(texto: str) -> str:
    """
    Metodo para generar un mensaje de error
    :arg
    :texto:texto del mensaje error

    :return
    :texto:texto e formato de error
    """
    return texto_color(texto, 'rojo')


def advertencia(texto: str) -> str:
    """
     Metodo para generar un mensaje de advertencia
    :arg
    :texto:texto del mensaje advertencia

    :return
    :texto:texto e formato de advertencia

    """
    return texto_color(texto, 'amarillo')


def info(texto: str) -> str:
    """
        Metodo para generar un mensaje de info
       :arg
       :texto:texto del mensaje info

       :return
       :texto:texto e formato de info

       """
    return texto_color(texto, 'azul')


def confirm(texto: str) -> str:
    """
        Metodo para generar un mensaje de confirm
       :arg
       :texto:texto del mensaje confirm

       :return
       :texto:texto e formato de confirm

       """
    return texto_color(texto, 'verde')


def texto_es_numero(valor: str) -> int:
    while True:
        if valor.isnumeric():
            return int(valor)
        else:
            print(texto_color(f"El texto {valor} no se puede convertir a numero", 'rojo'))
            print(advertencia('Ingrese nuevamente un numero:'))
            valor = input()
