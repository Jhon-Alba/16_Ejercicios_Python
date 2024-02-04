from datetime import datetime
import utils
from rich.console import Console

console = Console()

"""
 E05: En este problema Se ingresa un valor numérico de 8 dígitos que representa una fecha con el 
siguiente formato: aaaammdd. Esto es: los 4 primeros dígitos representan el año, los siguientes 2 
dígitos representan el mes y los 2 dígitos restantes representan el día. Se pide informar por 
separado el día, el mes y el año de la fecha ingresada. Para su solución se debe de hacer uso de 
divisiones, operador modulo y conversión de double a entero.
"""


def validar_fecha(cadena: str, formato: str = '%Y%m%d') -> bool:
    try:
        fecha = datetime.strptime(cadena, formato)
        return True
    except ValueError as msg_error:
        console.print(msg_error, style="bold red")
        return False


def extraer_fecha(fecha: int) -> ():
    if fecha >= 10000000 and fecha <= 99999999:
        if validar_fecha(str(fecha)):
            anio = fecha // 10000
            mes = (fecha % 10000) // 100
            dia = fecha % 100
            return anio, mes, dia
    return False


def menu_fecha():
    """
        Metodo para saber si una fecha es correcta
    """
    print("")
    console.print("-----FECHA-----", style="bold cyan")
    console.print("Ingrese una fecha en el formato YYYY-MM-DD", style="bold deep_pink3")
    numero = utils.texto_a_numero(input())
    resultado = extraer_fecha(numero)
    if resultado:
        console.print(f"El numero {numero} representa la fecha {resultado[2]}/{resultado[1]}/{resultado[0]}")


if __name__ == '__main__':
    menu_fecha()
