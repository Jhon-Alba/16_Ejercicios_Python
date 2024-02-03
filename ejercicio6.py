from rich.console import Console
import utils

console = Console()


def menu_numero_menor_mayor():
    print("")
    console.print("-----NUMERO DE MAYOR A MENOR-----", style="bold cyan")
    console.print("Ingrese el primer numero", style="bold deep_pink3")
    numero1 = utils.texto_a_numero(input())
    console.print("Ingrese el segundo numero", style="bold deep_pink3")
    numero2 = utils.texto_a_numero(input())
    console.print("Ingrese el tercer numero", style="bold deep_pink3")
    numero3 = utils.texto_a_numero(input())
    numero = [numero1, numero2, numero3]
    numero.sort()
    console.print("El numero mayor es: ", numero[2], "\nEl numero de en medio es: ", numero[1],"\nEl numero menor es: ", numero[0], style ="bold green4")


if __name__ == '__main__':
    menu_numero_menor_mayor()
