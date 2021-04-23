#Elaborado por: Maynor Martínez 2021052792
#Fecha de Creación: 12/04/2021 23:50 
#Fecha de última Modificación: 
#Versión: 3.9.2


from funciones import *
from validaciones import *

#----------------------------------------------------------------------#
#                           Entrada/Salida                             #
#----------------------------------------------------------------------#

#---CÓDIGO EUCALIPTO
def cifrarEucaliptoES():
    """
    Funcionamiento: Se encarga de la entrada, salida y validación de datos, además de mostrar un mensaje si ocurre un error
    Entradas:
    -NA
    Salidas: 
    -Mensajes informativos si ocurre errores
    -El código encriptado
    """
    texto = input("Ingrese la palabra que desea encriptar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a codificar.")
    elif not validarLetras(texto):
        print("No deben de haber caracteres especiales, ni números.")
    else:
        print("El código encriptado es: "+cifrarEucalipto(texto))
        añadirBitacora("Encriptar-Eucalipto",texto,descifrarEucalipto(texto))
    return False

def descifrarEucaliptoES():
    """
    Funcionamiento: Se encarga de la entrada, salida y validación de datos, además de mostrar un mensaje si ocurre un error
    Entradas:
    -NA
    Salidas: 
    -Mensajes informativos si ocurre errores
    -El código encriptado
    """
    texto = input("Ingrese la palabra que se desea desencriptar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a codificar.")
    elif not validarEucaliptoDescifrar(texto):
        print("Tiene un caracter inválido de códficar.")
    else:
        print("El código desencriptado es: "+descifrarEucalipto(texto))
    return False

#---CÓDIGO MORSE
def cifrarMorseES():
    """
    Funcionamiento: Se encarga de la entrada, salida y validación de datos, además de mostrar un mensaje si ocurre un error
    Entradas:
    -NA
    Salidas: 
    -Mensajes informativos si ocurre errores
    -El código encriptado
    """
    texto = input("Ingrese la palabra que desea encriptar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a codificar.")
    elif not validarMorseCifrar(texto):
        print("No deben de haber caracteres especiales o usa un caracter que no existe en morse.")
    else:
        print("El código encriptado es: "+cifrarMorse(texto))

    return False

def descifrarMorseES():
    """
    Funcionamiento: Se encarga de la entrada, salida y validación de datos, además de mostrar un mensaje si ocurre un error
    Entradas:
    -NA
    Salidas: 
    -Mensajes informativos si ocurre errores
    -El código encriptado
    """
    texto = input("Ingrese la palabra que desea desencriptar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a codificar.")
    elif not validarMorseDescifrar(texto):
        print("No sigue el formato de morse, los caracteres válidos son: '.-^|'")        
    else:
        print("El código encriptado es: "+descifrarMorse(texto))
    return False


##SUFAMELICO
def cifrarSufamelicoES():
    """
    Funcionamiento: Se encarga de la entrada, salida y validación de datos, además de mostrar un mensaje si ocurre un error
    Entradas:
    -NA
    Salidas: 
    -Mensajes informativos si ocurre errores
    -El código encriptado
    """
    texto = input("Ingrese la palabra que desea encriptar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a codificar.")
    elif not validarLetras(texto):
        print("No deben de haber caracteres especiales, ni números.")
    else:
        print("El código encriptado es: "+codigoSufamelico(texto))
    return False

def descifrarSufamelicoES():
    """
    Funcionamiento: Se encarga de la entrada, salida y validación de datos, además de mostrar un mensaje si ocurre un error
    Entradas:
    -NA
    Salidas: 
    -Mensajes informativos si ocurre errores
    -El código encriptado
    """
    texto = input("Ingrese la palabra que se desea desencriptar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a codificar.")
    else:
        print("El código desencriptado es: "+codigoSufamelico(texto))
    return False
