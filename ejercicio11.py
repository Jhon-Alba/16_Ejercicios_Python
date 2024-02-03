from rich.console import Console
import utils

console = Console()


def menu_invertir_numeros():
    console.print("-----INVERTIR NUMEROS DIGITADOS-----", style="bold cyan")
    console.print("Ingrese los numeros deseados", style="bold deep_pink3")
    numero = utils.texto_a_numero(input())
    numero = str(numero)
    numero_invertido = numero[::-1]
    console.print(f"Los numeros invertidos quedaron asi: {numero_invertido}", style="bold green4")


if __name__ == '__main__':
    menu_invertir_numeros()
