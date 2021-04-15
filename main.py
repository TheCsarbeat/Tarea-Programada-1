#Elaborado por: Maynor Martínez 2021052792
#Fecha de Creación: 12/04/2021 23:50 
#Fecha de última Modificación: 
#Versión: 3.9.2


from funciones import *
#----------------------------------------------------------------------#
#                           validaciones                               #
#----------------------------------------------------------------------#
def validarAlfabeto(texto):
    """
    Funcionamiento: Se encarga de la validaciones de l
    Entradas:NA
    Salidas: 
    -Un desgloce de la URL ingresada
    """
    if texto == "":
        return 'a'
    elif texto.isalnum() or (texto.isalpha and not(texto.isalpha())):
        return 'b'
    elif not(texto.isalnum()):
        return 'c'
    else:
        return True
    
def codificarEucaliptoES():    
    texto = input("Ingrese la palabra sin cifrar: ")
    if validarAlfabeto(texto) == True:
        print(codificarEucalipto(texto))        
    elif validarAlfabeto(texto) == "a":
        print("Debe escribir una palabra")
        if input("Ingrese 0 para salir: ") == 0:
            return""
        else:
            codificarEucaliptoES()
    elif validarAlfabeto(texto) == "b":
        print("El texto ingresado tiene número y no los podemos codificar")
        if input("Ingrese 0 para salir: ") == 0:
            return""
        else:
            codificarEucaliptoES()
    elif validarAlfabeto(texto) == "c":
        print("Los caracteres especiales no se pueden codificar")
        if input("Ingrese 0 para salir: ") == 0:
            return""
        else:
            codificarEucaliptoES()
            
codificarEucaliptoES()