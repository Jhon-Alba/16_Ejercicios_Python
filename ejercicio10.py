from rich.console import Console
import utils

console = Console()


def menu_segundos():
    console.print("-----SEGUNDOS INVERTIDOS EN EVALUACION-----", style="bold cyan")
    console.print("Ingrese los segundos invertidos", style="bold deep_pink3")
    segundos = utils.texto_a_numero(input())
    hora = segundos / 3600
    min = segundos % 60
    console.print(f"el tiempo que duro es {hora}h, {min} min", style="bold green4")


if __name__ == '__main__':
    menu_segundos()
