from rich.console import Console
import utils

console = Console()
"""
 E15: Pedir un número de 0 a 99 y mostrarlo escrito. Por ejemplo, para 56 mostrar: cincuenta y 
seis.
"""


def menu_palabras():
    """
        Metodo para convertir numeros a letras
    """
    console.print("-----CONVERTIR NUMEROS A LETRAS-----", style="bold cyan")
    console.print("Ingrese un numero entre 0 y 99", style="bold deep_pink3")
    numero = utils.texto_a_numero(input())
    if 0 <= numero <= 99:
        resultado = convertir_a_palabras(numero)
        console.print(f"El número {numero} se escribe como: {resultado}", style="bold green4")
    else:
        console.print("Número fuera de rango. Por favor, ingrese un número entre 0 y 99.", style="bold red")


def convertir_a_palabras(numero):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    especiales_10_19 = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho",
                        "diecinueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    if 0 <= numero <= 9:
        return unidades[numero]
    elif 10 <= numero <= 19:
        return especiales_10_19[numero - 10]
    elif 20 <= numero <= 99:
        decena = numero // 10
        unidad = numero % 10

        if unidad == 0:
            return decenas[decena]
        else:
            return decenas[decena] + " y " + unidades[unidad]


if __name__ == '__main__':
    menu_palabras()
