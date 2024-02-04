from rich.console import Console
import utils

console = Console()

"""
E02: En este problema tenemos un único dato de entrada: un valor numérico entero que deberá 
ingresar el usuario. La salida del algoritmo será informar si el usuario ingresó un valor par o impar. 
Sabemos que un número par es aquel que es divisible por 2 o, también, que un número es par si el 
valor residual que se obtiene al dividirlo por 2 es cero. Según lo anterior, podremos informar que 
el número ingresado por el usuario es par si al dividirlo por 2 obtenemos un resto igual a cero. De 
lo contrario, informaremos que el número es impar.
"""
def menu_par_o_impar():
    """
    Metodo para saber si un numero es par o impar
    """
    print("")
    console.print("----- PAR O IMPAR -----", style="cyan")
    console.print("Ingrese el numero entero deseado: ", style="deep_pink3")
    numero = utils.texto_a_numero(input())
    console.print(f"El numero {numero} es: " + str("par" if numero % 2 == 0 else "impar"), style="bold green4")


def par_o_impar(numero: int) -> bool:
    return numero % 2 == 0


if __name__ == '__main__':
    menu_par_o_impar()
