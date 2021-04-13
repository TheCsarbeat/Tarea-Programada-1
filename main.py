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
    validacion = True
    for i in texto: 
        if i == "":
            return False
        else:
            return validacion
def codigoEucaliptoES(opcion):

    if opcion == 1:
        texto = input("Ingrese el texto sin cifrar: ")
    else:
        texto = input("Ingrese el texto  cifrado: ")

    if validarAlfabeto(texto):
        print(procesarCodigoEucalipto(texto,opcion))
    else:
        codigoEucaliptoES(opcion)
        print("Debe escribir una palabra")
    codigoEucaliptoES(2)
codigoEucaliptoES(1)