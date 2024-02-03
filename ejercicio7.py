import utils
import math
from rich.console import Console

console = Console()


def menu_hipotenusa():
    console.print("-----CALCULAR HIPOTENUSA DE UN TRIANGULO-----", style="bold cyan")
    console.print("Ingrese el primer cateto", style="bold deep_pink3")
    cateto1 = utils.texto_a_numero(input())
    console.print("Ingrese el segundo cateto", style="bold deep_pink3")
    cateto2 = utils.texto_a_numero(input())
    h = ((cateto1 * cateto1) + (cateto2 * cateto2))
    console.print(f"El resultado de la hipotenusa es: {h}", style="bold green4")


if __name__ == '__main__':
    menu_hipotenusa()
