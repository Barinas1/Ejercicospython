# This is a sample Python script.
from color_texto import info, advertencia, texto_es_numero, error, texto_color
import Ejercicio01 , Ejercicio02 ,Ejercicio03,Ejercicio04,Ejercicio05y08,Ejercicio06,Ejercicio07,Ejercicio09,Ejercicio10,Ejercicio11,Ejercicio12,Ejercicio13,Ejercicio14,Ejercicio15,Ejercicio16


def menu():
    while True:
        print('')
        print(texto_color('---- Menu Principal ----','blanco'))
        print(info("Seleccione un ejercicio a ejecutar:"))
        print(info("1)Cociente de dos numeros"))
        print(info("2)Numero es par o impar"))
        print(info("3)Radio de un circulo"))
        print(info("4)Multiplo de 2 y 3"))
        print(info("5)Mostrar fecha en formato de año,mes y dia"))
        print(info("6)Numero Mayor,Medio,Menor"))
        print(info("7)Calcular hipotenusa"))
        print(info("9)Numero mes"))
        print(info("10)Tiempo que una persona gasta al hacer un examen"))
        print(info("11)Numero inverso"))
        print(info("12)Numero es capicua o no"))
        print(info("13)Cantidad de veces de un numero aparece en caracter"))
        print(info("14)Cadena de caracteres es palíndroma"))
        print(info("16)Cadena capitalizar"))
        print(info("17)Salir"))
        print('')
        opcion = texto_es_numero(input())
        if opcion == 1:
            Ejercicio01.calcular_cociente()
        elif opcion == 2:
            Ejercicio02.par_impar()
        elif opcion == 3:
            Ejercicio03.calcular_area_circulo()
        elif opcion == 4:
            Ejercicio04.verificar_multiplo_2_y_3()
        elif opcion == 5:
            Ejercicio05y08.obtener_fecha()
        elif opcion == 6:
            Ejercicio06.verificar_numero()
        elif opcion == 7:
            Ejercicio07.calcular_catetos()
        elif opcion == 9:
            Ejercicio09.mes()
        elif opcion == 10:
            Ejercicio10.tiempo()
        elif opcion == 11:
            Ejercicio11.numero_inverso()
        elif opcion == 12:
            Ejercicio12.calcular_numero()
        elif opcion == 13:
            Ejercicio13.calcular_caracter()
        elif opcion == 14:
            Ejercicio14.verificar_cadena()
        elif opcion == 15:
            Ejercicio15.numero_en_palabra()
        elif opcion == 16:
            Ejercicio16.cadena_capitalizar()
        elif opcion == 17:
            print(info("Programa Finalizado..."))
            exit(0)
        else:
            print(error('Opción no encontrada debe estar entre 1 y 30'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(texto_color('Bienvenido al desarrollo del taller de logica de programación con python','magenta'))
    print(texto_color('Nombres:Marien julieta Barinas Alarcón','magenta'))
    print(texto_color('Ficha:2670142','magenta'))
    print('')
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
