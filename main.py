import ejercicio10
import ejercicio11
import ejercicio12
import ejercicio13
import ejercicio14
import ejercicio15
import ejercicio16
import ejercicio5_8
import ejercicio6
import ejercicio7
import ejercicio9
import utils
from rich.console import Console
from rich.table import Table
import ejercicio1
import ejercicio2
import ejercicio3
import ejercicio4

console = Console()


# Probar en terminal, ahi se ven los colores
def menu():
    while True:
        print("")
        console.print("MENU PRINCIPAL", style="bold cyan")
        table = Table(title="Digite una opcion para iniciar el programa", style="cyan")
        table.add_column("Numero", style="bold underline medium_purple1", justify="center")
        table.add_column("Opcion", style="bold underline medium_purple1", justify="left")

        table.add_row("1", "Division de 2 numeros")
        table.add_row("2", "Par o impar")
        table.add_row("3", "Area del circulo")
        table.add_row("4", "Multiplo de 2 y 3")
        table.add_row("5", "Validar fecha")
        table.add_row("6", "Numero de mayor a menor")
        table.add_row("7", "Calcular hipotenusa de un triangulo")
        table.add_row("8", "Validar fecha")
        table.add_row("9", "Mes")
        table.add_row("10", "Segundos invertidos en un examen")
        table.add_row("11", "Numeros invertidos")
        table.add_row("12", "Numero par y capicua")
        table.add_row("13", "Contar un caracter en una cadena de caracteres")
        table.add_row("14", "Saber si una palabra es palindroma")
        table.add_row("15", "Convertir numeros a letras")
        table.add_row("16", "Capitalizar una frase")
        table.add_row("0", "Salir")
        console.print(table)
        console.print("Digite aqui: ", style="bold underline medium_purple1")
        opcion = utils.texto_a_numero(input())
        if opcion == 1:
            ejercicio1.menu_division()
        elif opcion == 2:
            ejercicio2.menu_par_o_impar()
        elif opcion == 3:
            ejercicio3.menu_area()
        elif opcion == 4:
            ejercicio4.menu_multiplo_2_3()
        elif opcion == 5:
            ejercicio5_8.menu_fecha()
        elif opcion == 6:
            ejercicio6.menu_numero_menor_mayor()
        elif opcion == 7:
            ejercicio7.menu_hipotenusa()
        elif opcion == 8:
            ejercicio5_8.menu_fecha()
        elif opcion == 9:
            ejercicio9.menu_mes()
        elif opcion == 10:
            ejercicio10.menu_segundos()
        elif opcion == 11:
            ejercicio11.menu_invertir_numeros()
        elif opcion == 12:
            ejercicio12.menu_par_capicua()
        elif opcion == 13:
            ejercicio13.menu_contar_caracter()
        elif opcion == 14:
            ejercicio14.menu_palabra_palindroma()
        elif opcion == 15:
            ejercicio15.menu_palabras()
        elif opcion == 16:
            ejercicio16.menu_frase()
        elif opcion == 0:
            console.print("El programa ha termidado correctamente :smiley:", style="bold green4")
            exit(0)


if __name__ == '__main__':
    console.print("BIENVENID@ AL PROGRAMA", style="bold cyan")
    menu()
