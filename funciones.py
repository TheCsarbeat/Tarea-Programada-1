#Creado por: César Jiménez Salazar
#Fecha de realización:14/04/2021 08:39 p.m.
#Última modificación:14/04/2021 03:39  p.m.
#Versión: 3.8.2

def validarEntradaCifrado(texto):
    lista = texto.split()
    for i in range(len(lista)):
        if not lista[i].isalpha():
            return False
    return True
def cifrarMurcielago(texto):
    """
    Funcionamiento: cifra el texto al código murciélago usado por los scouts
    Entradas: -texto: el texto a cifrar del usuario
    Salidas: retorna el texto cifrado en código murciélago
    """
    impresion = ""
    for i in range(len(texto)):
        if texto[i].lower() == "m":
            impresion+="0"
        elif texto[i].lower() == "u":
            impresion+="1"
        elif texto[i].lower() == "r":
            impresion+="2"
        elif texto[i].lower() == "c":
            impresion+="3"
        elif texto[i].lower() == "i":
            impresion+="4"
        elif texto[i].lower() == "e":
            impresion+="5"
        elif texto[i].lower() == "l":
            impresion+="6"
        elif texto[i].lower() == "a":
            impresion+="7"
        elif texto[i].lower() == "g":
            impresion+="8"
        elif texto[i].lower() == "o":
            impresion+="9"
        elif texto[i] == " ":
            impresion+="*"
        else:
            impresion+=texto[i]
    return impresion

def descifrarMurcielago(texto):
    """
    Funcionamiento: descifra el texto en código muerciélago a su equivalente español
    Entradas: -texto: el texto a descifrar del usuario
    Salidas: retorna el texto descifrado del murciélago de entrada
    """
    impresion = ""
    for i in range(len(texto)):
        if texto[i].lower() == "0":
            impresion+="m"
        elif texto[i].lower() == "1":
            impresion+="u"
        elif texto[i].lower() == "2":
            impresion+="r"
        elif texto[i].lower() == "3":
            impresion+="c"
        elif texto[i].lower() == "4":
            impresion+="i"
        elif texto[i].lower() == "5":
            impresion+="e"
        elif texto[i].lower() == "6":
            impresion+="l"
        elif texto[i].lower() == "7":
            impresion+="a"
        elif texto[i].lower() == "8":
            impresion+="g"
        elif texto[i].lower() == "9":
            impresion+="o"
        elif texto[i] == "*":
            impresion+=" "
        else:
            impresion+=texto[i]
    return impresion

