#Elaborado por: Maynor Martínez 2021052792
#Fecha de Creación: 12/04/2021 23:50 
#Fecha de última Modificación: 
#Versión: 3.9.2


from funciones import *
from validaciones import *
from datetime import datetime
def bitacora(proceso,entrada,salida):
    ahora = datetime.now()
    bitacora = open("Bitacora.txt","w")
    bitacora.write("A las "+str(ahora.time())+" se ejecutó \t"+proceso+": entrada("+entrada+"), salida("+salida+")\n")
    bitacora.close()
#----------------------------------------------------------------------#
#                           Entrada/Salida                             #
#----------------------------------------------------------------------#

#---CÓDIGO EUCALIPTO
def encriptarEucaliptoES():
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
        print("El código encriptado es: "+codificarEucalipto(texto))
        bitacora("Encriptar-Eucalipto",texto,codificarEucalipto(texto))
    return False

def desencriptarEucaliptoES():
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
    elif not validarDesencriptarEucalipto(texto):
        print("Tiene un caracter inválido de códficar.")
    else:
        print("El código desencriptado es: "+decodificarEucalipto(texto))
    return False

#---CÓDIGO MORSE
def encriptarMorseES():
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
    elif not validarMorseEncriptacion(texto):
        print("No deben de haber caracteres especiales o usa un caracter que no existe en morse.")
    else:
        print("El código encriptado es: "+encriptarMorse(texto))

    return False

def desencriptarMorseES():
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
    elif not validarMorseDesencriptacion(texto):
        print("No sigue el formato de morse, los caracteres válidos son: '.-^|'")        
    else:
        print("El código encriptado es: "+desencriptarMorse(texto))
    desencriptarMorseES() 
    return False


##SUFAMELICO
def encriptarSufamelicoES():
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

def desencriptarSufamelicoES():
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

encriptarSufamelicoES()
desencriptarSufamelicoES()