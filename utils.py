from rich.console import Console

console = Console()


def entero(msg: str = None) -> int:
    valor = input(msg if msg is not None else "Ingrese un numero entero")
    while True:
        try:
            return int(valor)
        except ValueError:
            console.print(f"El texto {valor} no se puede convertir")
            valor = input("Ingrese nuevamente los digitos: ")


def texto_a_numero(valor: str):
    """
    Metodo para validar caracteres
    """
    while True:
        if valor.isnumeric():
            return int(valor)
        else:
            console.print(f"El siguiente texto {valor} no se puede convertir a numero", style="bold red")
            console.print("Ingrese nuevamente un numero", style="bold red")
            valor = input()
