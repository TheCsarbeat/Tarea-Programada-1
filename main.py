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
    texto = input("Ingrese la palabra que desea cifrar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a cifrar.")
    elif not validarLetras(texto):
        print("No deben de haber caracteres especiales, ni números.")
    else:
        print("El código cifrado es: "+cifrarEucalipto(texto))
        añadirBitacora("Eucalipto-Descifrar",texto,cifrarEucalipto(texto))
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
    texto = input("Ingrese la palabra que se desea decifrar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a descifrar.")
    elif not validarEucaliptoDescifrar(texto):
        print("Tiene un caracter inválido.")
    else:
        print("El código descifrado es: "+descifrarEucalipto(texto))
        añadirBitacora("Eucalipto-Cifrar",texto,descifrarEucalipto(texto))
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
    texto = input("Ingrese la palabra que desea cifrar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a cifrar.")
    elif not validarMorseCifrar(texto):
        print("No deben de haber caracteres especiales o usa un caracter que no existe en morse.")
    else:
        print("El código cifrado es: "+cifrarMorse(texto))
        añadirBitacora("Morse-Cifrar",texto,cifrarMorse(texto))
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
    texto = input("Ingrese la palabra que desea descifrar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a descifrar.")
    elif not validarMorseDescifrar(texto):
        print("No sigue el formato de morse, los caracteres válidos son: '.-^|'")        
    else:
        print("El código descifrado es: "+descifrarMorse(texto))
        añadirBitacora("Morse-Descifrar",texto,descifrarMorse(texto))
    return False

#SUFAMELICO
def cifrarSufamelicoES():
    """
    Funcionamiento: Se encarga de la entrada, salida y validación de datos, además de mostrar un mensaje si ocurre un error
    Entradas:
    -NA
    Salidas: 
    -Mensajes informativos si ocurre errores
    -El código cifrado
    """
    texto = input("Ingrese la palabra que desea cifrar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a cifrar.")
    elif not validarLetras(texto):
        print("No deben de haber caracteres especiales, ni números.")
    else:
        print("El código descifrado es: "+codigoSufamelico(texto))
        añadirBitacora("Sufamélico-Cifrar",texto,codigoSufamelico(texto))
    return False

def descifrarSufamelicoES():
    """
    Funcionamiento: Se encarga de la entrada, salida y validación de datos, además de mostrar un mensaje si ocurre un error
    Entradas:
    -NA
    Salidas: 
    -Mensajes informativos si ocurre errores
    -El código descifrado
    """
    texto = input("Ingrese la palabra que se desea descifrar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a descifrar.")
    else:
        print("El código cifrado es: "+codigoSufamelico(texto))
        añadirBitacora("Sufamélico-Descifrar",texto,codigoSufamelico(texto))
    return False
descifrarSufamelicoES()