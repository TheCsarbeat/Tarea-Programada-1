#Creado por: César Jiménez Salazar
#Fecha de realización:14/04/2021 08:39 p.m.
#Última modificación:14/04/2021 11:13  p.m.
#Versión: 3.8.2
from funciones import *
from validaciones import *
#Declaración de funciones

def cifrarMurcielagoES():
    """
    Funcionamiento: pide al usuario el texto a cifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto cifrado
    """
    texto = input("Ingrese el texto a cifrar: ")
    if validarLetras(texto) and validarVacio(texto):
        return print("Su texto cifrado en código murciélago es: "+cifrarMurcielago(texto))
    else:
        return print("Entrada inválida, no ingrese caracteres especiales ni números")
    
def descifrarMurcielagoES():
    """
    Funcionamiento: pide al usuario el texto a descifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto descifrado
    """
    texto = input("Ingrese el texto a descifrar: ")
    if validarMurcielago(texto) and validarVacio(texto):
        return print("Su texto descifrado del código murciélago es: "+descifrarMurcielago(texto))
    else:
        return print("El código que ingresó no es válido, intente con el formato h967*70489")

def cifrarCenitPolarES():
    """
    Funcionamiento: pide al usuario el texto a descifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto descifrado
    """
    texto = input("Ingrese el texto a cifrar: ")
    if validarLetras(texto) and validarVacio(texto):
        return print("Su texto cifrado en código cenit polar es: "+cifrarCenitPolar(texto))
    else:
        return print("Entrada inválida, no ingrese caracteres especiales ni números")

def descifrarCenitPolarES():
    """
    Funcionamiento: pide al usuario el texto a descifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto descifrado
    """
    texto = input("Ingrese el texto a descifrar: ")
    if validarCenit(texto) and validarVacio(texto):
        return print("Su texto descifrado del cenit polar es: "+cifrarCenitPolar(texto))
    else:
        return print("El código que ingresó no es válido, intente con el formato heni¬image")

def cifrarDeletreoES():
    """
    Funcionamiento: pide al usuario el texto a descifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto descifrado
    """
    texto = input("Ingrese el texto a cifrar: ")
    if validarDeletreoCifrar(texto) and validarVacio(texto):
        return print("Su texto cifrado en código deletreo es: "+cifrarDeletreo(texto))
    else:
        return print("Entrada inválida, no ingrese caracteres especiales ni números")

def descifrarDeletreoES():
    """
    Funcionamiento: pide al usuario el texto a descifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto descifrado
    """
    texto = input("Ingrese el texto a descifrar: ")
    if validarDeletreoDescifrar(texto) and validarVacio(texto):
        return print("Su texto descifrado del código murciélago es: "+descifrarDeletreo(texto))
    else:
        return print("El código que ingresó no es válido, intente con el formato Oscar~Lima~Alfa")


#cifrarMurcielagoES()
#descifrarMurcielagoES()
#cifrarCenitPolarES()
#descifrarCenitPolarES()
#cifrarDeletreoES()
#descifrarDeletreoES()
