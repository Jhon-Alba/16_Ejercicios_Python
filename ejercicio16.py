from rich.console import Console

console = Console()
"""
 E16: Desarrollar un algoritmo que solicite una frase de mínimo 5 palabras y capitalizar la cadena.
"""


def menu_frase():
    """
        Metodo para capitalizar una frase
    """
    console.print("-----CAPITALIZAR UNA FRASE-----", style="bold cyan")
    while True:
        console.print("Ingrese una frase de al menos 5 palabras", style="bold deep_pink3")
        frase = (input())
        if len(frase.split()) >= 5:
            frase_capitalizada = frase.title()
            print(f"La frase capitalizada es: {frase_capitalizada}")
            break
        else:
            print("La frase debe tener al menos 5 palabras digite nuevamente")


if __name__ == '__main__':
    menu_frase()
