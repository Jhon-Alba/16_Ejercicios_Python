from rich.console import Console
import utils

console = Console()
"""
E10: Dado un número (leído por teclado), que representa los segundos que ha invertido una 
persona en hacer un examen, determinar cuántas horas, minutos y segundos ha invertido. 
Imprima el resultado por pantalla.
"""


def menu_segundos():
    """
        Metodo para saber cuantos horas y minutos invirtio en una evaluacion
    """
    console.print("-----SEGUNDOS INVERTIDOS EN EVALUACION-----", style="bold cyan")
    console.print("Ingrese los segundos invertidos", style="bold deep_pink3")
    segundos = utils.texto_a_numero(input())
    hora = segundos / 3600
    min = segundos % 60
    console.print(f"el tiempo que duro es {hora}h, {min} min", style="bold green4")


if __name__ == '__main__':
    menu_segundos()
