from rich.console import Console

console = Console()


def menu_contar_caracter():
    console.print("-----CONTAR CARACTER-----", style="bold cyan")
    console.print("Ingrese una cadena de caracteres", style="bold deep_pink3")
    cadena = input()
    console.print("Ingrese el caracter que desea contar", style="bold deep_pink3")
    caracter = input()
    contador = cadena.count(caracter)
    caracter.upper()
    console.print(f"El caracter {caracter.upper()}, aparece {contador} vez(ces) en el texto", style="bold green4")


if __name__ == '__main__':
    menu_contar_caracter()
