from rich.console import Console
import utils

console = Console()

"""
 E04: En este problema tenemos un único dato de entrada: un valor numérico entero que deberá 
ingresar el usuario. La salida del algoritmo será informar si el numero ingresado por el usuario es 
múltiplo de 2 y 3. Sabemos que un número es múltiplo de otro cuando al dividir estos dos 
números el residuo sea 0. Si el usuario ingresó un valor negativo o cero tendremos que emitir un 
mensaje informando las causas por las cuales no se podrá efectuar la operación.
"""


def menu_multiplo_2_3():
    """
    Metodo para saber si un numero es multiplo de 2 y 3
    """
    print("")
    console.print("----- MULTIPLO DE 2 Y 3 -----", style="bold cyan")
    console.print("Ingrese el numero deseado:", style="bold deep_pink3")
    numero = utils.texto_a_numero(input())
    console.print(f"El numero {numero} " + str(
        "es multiplo de 2 y 3" if numero % 2 == 0 or numero % 3 == 0 else "no es multiplo de 2 y 3"),
                  style="bold green4")


def calcular_multiplo_2_3(numero: int):
    if numero > 0:
        if numero % 2 == 0 or numero % 3 == 0:
            console.print(f"El numero {numero} es multiplo de 2 y 3", style="bold green4")
        else:
            console.print(f"El numero {numero} no es multiplo de 2 y 3", style="bold green4")
    else:
        console.print("Ingrese un numero mayor a 0", style="bold red")


if __name__ == '__main__':
    menu_multiplo_2_3()
