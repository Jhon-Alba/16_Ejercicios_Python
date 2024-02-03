from rich.console import Console
import utils

console = Console()


def menu_division():
    """
    Metodo para dividir 2 numeros
    """
    print("")
    console.print("----- DIVISION DE 2 NUMEROS -----", style="bold cyan")

    console.print("Ingrese el primer numero entero: ", style="bold deep_pink3")
    numero1 = utils.texto_a_numero(input())
    console.print("Ingrese el segundo numero entero: ", style="bold deep_pink3")
    numero2 = utils.texto_a_numero(input())
    console.print(f"El resultado es: {calcular_division(numero1, numero2)}", style="bold green4")


def calcular_division(numero1: int, numero2: int) -> float:
    if numero2 == 0:
        console.print("La division por 0 no puede ser", style="bold red")
        return 0
    else:
        return numero1 / numero2


if __name__ == '__main__':
    menu_division()
