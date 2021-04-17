#Creado por: César Jiménez Salazar
#Fecha de realización:14/04/2021 08:39 p.m.
#Última modificación:14/04/2021 11:13  p.m.
#Versión: 3.8.2
from funciones import *
#Declaración de funciones

def cifrarMurcielagoES():
    """
    Funcionamiento: pide al usuario el texto a cifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto cifrado
    """
    texto = input("Ingrese el texto a cifrar: ")
    if validarEntradaCifrado(texto):
        return print("Su texto cifrado en código murciélago es: "+cifrarMurcielago(texto))
    else:
        return print("Entrada inválida, no ingrese caracteres especiales ni números")
    cifrarMurcielagoES()
def descifrarMurcielagoES():
    """
    Funcionamiento: pide al usuario el texto a descifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto descifrado
    """
    texto = input("Ingrese el texto a descifrar: ")
    return print("Su texto descifrado del código murciélago es: "+descifrarMurcielago(texto))

