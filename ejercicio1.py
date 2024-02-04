from rich.console import Console
import utils


console = Console()
"""
 E01: En este problema, los datos de entrada son los dos valores enteros que ingresará el usuario a 
través del teclado (los llamaremos a y b) y la salida será su cociente (un número flotante). Ahora 
bien, existe la posibilidad de que el usuario ingrese como segundo valor el número 0 (cero). En 
este caso, no podremos mostrar el cociente ya que la división por cero es una indeterminación, así 
que tendremos que emitir un mensaje informando las causas por las cuales no se podrá efectuar 
la operación.
"""

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
