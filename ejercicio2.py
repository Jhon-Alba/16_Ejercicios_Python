from rich.console import Console
import utils

console = Console()


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
