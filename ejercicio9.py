from rich.console import Console
import utils

console = Console()

"""
 E09: Se debe de ingresar un numero comprendido entre 1 y 12 por el usuario. El algoritmo debe 
de imprimir el mes correspondiente en texto.
"""


def menu_mes():
    """
        Metodo para saber a que numero le corresponde el mes
    """
    console.print("-----MESES-----", style="bold cyan")
    console.print("Ingrese el digito deseado", style="bold deep_pink3")
    mes = utils.texto_a_numero(input())
    meses = [" ", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
             "Noviembre", "Diciembre"]
    if mes > 12 or mes == 0:
        console.print("Digite nuevamente la opcion", style="bold red")
    else:
        console.print(f"El numero {mes} corresponde al mes de {meses[mes]} ", style="bold green4")


if __name__ == '__main__':
    menu_mes()
