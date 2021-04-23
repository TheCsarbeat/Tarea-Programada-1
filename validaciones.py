#Elaborado por: Maynor Martínez 2021052792
#Fecha de Creación: 21/04/2021 5:30 pm 
#Fecha de última Modificación: 
#Versión: 3.9.2

    ##Validaciones generales 

def validarVacio(texto):
    """
    Funcionamiento: Determina si la valiarble es vacía
    Entradas:
    -texto(string): la varaiable a validar 
    Salidas: 
    -True: si no es vacio
    -False: si es vacío
    """
    if texto!="":
        return True
    else:
        return False

def validarEspacios(texto): 
    """
    Funcionamiento: Determina si la variable contiene solo espacios
    Entradas:
    -texto(string): La varaiable a validar 
    Salidas: 
    -True: Si contiene solo espacios
    -False: En cualquier otro caso
    """
    if texto.isspace():
        return True
    else:
        return False

def validarLetras(texto):
    """
    Funcionamiento: Determina si es texto, sin caracteres especiales ni números, solo letras y espacios
    Entradas:
    -texto(string): La varaiable a validar 
    Salidas: 
    -True: Si es solo texto
    -False: En cualquier otro caso
    """
    for i in texto:
        if (i.isalpha()== False) and not(i in ",. "):
            return False
        elif i.isalpha == False:
            return False
    return True



def validarEucaliptoDescifrar(texto):
    """
    Funcionamiento: Determina si es válido para desencriptarlo
    Entradas:
    -texto(string): La varaiable a validar 
    Salidas: 
    -True: Si es valido a desencriptar
    -False: En cualquier otro caso
    """
    for i in texto:
        if (i.isalnum()== False) and not(i in ",.°"):
            return False
        elif i == "0":
            return False
    return True


def validarMorseCifrar(texto):
    """
    Funcionamiento: Determina si es texto, sin caracteres especiales, solo alfanúmericos y espacios
    Entradas:
    -texto(string): La varaiable a validar 
    Salidas: 
    -True: Si de la condición dada
    -False: En cualquier otro caso
    """
    texto = texto.lower()
    for i in texto:
        if not i.isalnum() and i != " ":
            return False
        elif i.isalpha()== True and i in "áéíóúñ":
            print(i)
            return False
    return True

def validarMorseDescifrar(texto):
    """
    Funcionamiento: Determina si es texto, sin caracteres especiales, solo alfanúmericos y espacios
    Entradas:
    -texto(string): La varaiable a validar 
    Salidas: 
    -True: Si de la condición dada
    -False: En cualquier otro caso
    """
    cont =0
    for i in texto:
        if not(i in ".-^|"):
            print(i+str(cont))
            return False
        cont+=1
    return True