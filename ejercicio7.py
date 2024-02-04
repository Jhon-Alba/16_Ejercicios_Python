import utils
from rich.console import Console

console = Console()

"""
E07: Calcular la hipotenusa de un triángulo, teniendo como base el valor del cateto 1 y 2 que serán 
dados por el usuario. Para esto debe de hacer uso del Teorema de Pitágoras en el cálculo de la 
hipotenusa teniendo los catetos. (h= √(a^2 )+b^2) no se debe hacer uso de la librería Math.hypot
"""


def menu_hipotenusa():
    """
        Metodo para calcular la hiptenusa de un triangulo
    """
    console.print("-----CALCULAR HIPOTENUSA DE UN TRIANGULO-----", style="bold cyan")
    console.print("Ingrese el primer cateto", style="bold deep_pink3")
    cateto1 = utils.texto_a_numero(input())
    console.print("Ingrese el segundo cateto", style="bold deep_pink3")
    cateto2 = utils.texto_a_numero(input())
    h = ((cateto1 * cateto1) + (cateto2 * cateto2))
    console.print(f"El resultado de la hipotenusa es: {h}", style="bold green4")


if __name__ == '__main__':
    menu_hipotenusa()
