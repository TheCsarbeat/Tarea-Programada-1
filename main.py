#Creado por: César Jiménez Salazar
#Fecha de realización:14/04/2021 08:39 p.m.
#Última modificación:14/04/2021 11:13  p.m.
#Versión: 3.8.2
from funciones import *
from validaciones import *
#----------------------------------------------------------------------#
#                           Entrada/Salida                             #
#----------------------------------------------------------------------#

#---CÓDIGO murcielago
def cifrarMurcielagoES():
    """
    Funcionamiento: pide al usuario el texto a cifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto cifrado
    """
    texto = input("Ingrese la palabra que desea cifrar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a cifrar.")
    elif not validarLetras(texto):
        print("No deben de haber caracteres especiales, ni números.")
    else:
        print("El código cifrado es: "+cifrarMurcielago(texto))
        añadirBitacora("Murcielago-Cifrar",texto,cifrarMurcielago(texto))
    return False
def descifrarMurcielagoES():
    """
    Funcionamiento: pide al usuario el texto a descifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto descifrado
    """
    texto = input("Ingrese el texto a descifrar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a descifrar.")
    elif not validarMurcielago(texto):
        print("Tiene un caracter inválido.")
    else:
        print("El código descifrado es: "+descifrarMurcielago(texto))
        añadirBitacora("Murcielago-Descifrar",texto,descifrarMurcielago(texto))
    return False
#---CÓDIGO Cenit polar
def cifrarCenitPolarES():
    """
    Funcionamiento: pide al usuario el texto a cifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto cifrado
    """
    texto = input("Ingrese la palabra que desea cifrar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a cifrar.")
    elif not validarLetras(texto):
        print("No deben de haber caracteres especiales, ni números.")
    else:
        print("El código cifrado es: "+cifrarCenitPolar(texto))
        añadirBitacora("CenitPolar-Cifrar",texto,cifrarCenitPolar(texto))
    return False
def descifrarCenitPolarES():
    """
    Funcionamiento: pide al usuario el texto a descifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto descifrado
    """
    texto = input("Ingrese el texto a descifrar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a descifrar.")
    elif not validarCenit(texto):
        print("Tiene un caracter inválido.")
    else:
        print("El código descifrado es: "+cifrarCenitPolar(texto))
        añadirBitacora("CenitPolar-Descifrar",texto,cifrarCenitPolar(texto))
    return False
#---CÓDIGO Deletreo
def cifrarDeletreoES():
    """
    Funcionamiento: pide al usuario el texto a cifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto cifrado
    """
    texto = input("Ingrese la palabra que desea cifrar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif not validarDeletreoCifrar(texto):
        print("Solo puede ser una palabra, únicamente letras")
    else:
        print("El código cifrado es: "+cifrarDeletreo(texto))
        añadirBitacora("Deletreo-Cifrar",texto,cifrarDeletreo(texto))
def descifrarDeletreoES():
    """
    Funcionamiento: pide al usuario el texto a descifrar
    Entradas:
    Salidas: retorna la impresión al usuario del texto descifrado
    """
    texto = input("Ingrese el texto a descifrar: ")
    if not validarVacio(texto):
        print("Debe ingresar un texto")
    elif  validarEspacios(texto):
        print("La cadena no contiene un mensaje a descifrar.")
    elif not validarDeletreoDescifrar(texto):
        print("Tiene un caracter inválido.")
    else:
        print("El código descifrado es: "+descifrarDeletreo(texto))
        añadirBitacora("Deletreo-Descifrar",texto,descifrarDeletreo(texto))
    return False
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
        añadirBitacora("Eucalipto-Cifrar",texto,cifrarEucalipto(texto))
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
        añadirBitacora("Eucalipto-Descifrar",texto,descifrarEucalipto(texto))
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

def menu():
    clearScreen()
    print("#---------------------------------------------------------------#")
    print("  Convertidor de español a códigos, claves y señales de pista")
    print("#---------------------------------------------------------------#")
    print("1.Clave Murciélago")
    print("2.Clave Eucalipto")
    print("3.Clave Cenit Polar")
    print("4.Código Morse")
    print("5.Clave Sufamélico")
    print("6.Clave Deletreo")
    print("7.Salir\n")
    opcion1 = input("Seleccione la opción que desee: ")
    if validarEntero(opcion1):
        opcion1 = int(opcion1)
        if opcion1 == 7:
            return ""
        elif opcion1 <= 6 and opcion1 > 0:
            opcion2 = input("1.Cifrar\n2.Descifrar\n\nSelecione la opción que desee: ")
            if validarEntero(opcion2):
                opcion2 = int(opcion2)
                if opcion2 <= 2 and opcion2 > 0:
                    subMenu(opcion1,opcion2)
                else:
                    print("Opción fuera de rango")
            else:
                print("Entrada inválida, ingrese el número de una de las opciones")        
        else:
            print("Opción fuera de rango") 
    else:
        print("Entrada inválida, ingrese el número de una de las opciones")
    input("Presione ENTER para continuar...")
    menu()

def subMenu(opcion1,opcion2):
    """
    Funcionamiento:Se encarga de llamar la función de entreda y salida correspondiente
    Entradas:
    -opcion1(int): La opción que contiene el tipo de código a usar
    -opcion1(int): La opción que contiene si quiere cifrar o descifrar
    Salidas: 
    -El resultado de la operación elegida
    """
    if opcion1 == 1:
        if opcion2 == 1:
            cifrarMurcielagoES()
        else:
            descifrarMurcielagoES()
    elif opcion1 == 2:
        if opcion2 == 1:
            cifrarEucaliptoES()
        else:
            descifrarEucaliptoES()
    elif opcion1 == 3:
        if opcion2 == 1:
            cifrarCenitPolarES()
        else:
            descifrarCenitPolarES()           
    elif opcion1 == 4:
        if opcion2 == 1:
            cifrarMorseES()
        else:
            descifrarMorseES()           
    elif opcion1 == 5:
        if opcion2 == 1:
            cifrarSufamelicoES()
        else:
            descifrarSufamelicoES()
    else:
        if opcion2 == 1:
            cifrarDeletreoES()
        else:
            descifrarDeletreoES()
            
menu()
