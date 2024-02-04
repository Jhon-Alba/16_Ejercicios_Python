from rich.console import Console

console = Console()

"""
 E14: Desarrollar un algoritmo que determine si una cadena de caracteres es palíndroma. Una 
cadena se dice palíndromo si al invertirla es igual a ella misma
"""


def menu_palabra_palindroma():
    """
        Metodo para saber si una palabra es palindroma
    """
    console.print("-----SABER SI UNA PALABRA ES PALINDROMA-----", style="bold cyan")
    console.print("Ingrese la palabra a verificar", style="bold deep_pink3")
    palabra = input()
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        console.print(f"La palabra {palabra} es palindroma", style="bold green4")
    else:
        console.print(f"La palabra {palabra} no es palindroma", style="bold green4")


if __name__ == '__main__':
    menu_palabra_palindroma()
