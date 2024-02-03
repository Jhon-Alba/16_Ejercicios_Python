from rich.console import Console
import utils

console = Console()


def menu_par_capicua():
    console.print("-----NUMERO PAR Y CAPICUA-----", style="bold cyan")
    console.print("Ingrese el numero deseado", style="bold deep_pink3")
    numero = utils.texto_a_numero(input())
    console.print(f"El numero {numero} es capicua?:  {numeroCapicua(numero)}", style="bold green4")
    console.print(f"El numero {numero} es: " + str("par" if numero % 2 == 0 else "impar"), style="bold green4")


def par_o_impar(numero: int) -> bool:
    return numero % 2 == 0


def numeroCapicua(numero):
    if not isinstance(numero, int):
        return None
    numero = str(numero)
    return numero == numero[::-1]


if __name__ == '__main__':
    menu_par_capicua()
