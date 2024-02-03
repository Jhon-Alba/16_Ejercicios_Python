from rich.console import Console
import utils

console = Console()


def menu_area():
    """
    Metodo para calcular el area de un circulo
    """
    print("")
    console.print("----- AREA DEL CIRCULO -----", style="bold cyan")
    console.print("Ingrese el dato del radio del circulo: \n", style="bold deep_pink3")
    numero = utils.texto_a_numero(input())
    resultado = calcular_area_circulo(numero)
    if resultado:
        console.print(f"El area del circulo es {resultado}", style="bold green4")
    else:
        console.print("No se puede calcular el area del circulo", style="bold red")


def calcular_area_circulo(numero: int or float) -> bool or float:
    if numero <= 0:
        console.print("El valor ingresado debe ser mayor a 0", style="bold red")
        return False
    else:
        return 3.1416 * (numero * numero)


if __name__ == '__main__':
    menu_area()
