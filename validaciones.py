#Creado por: César Jiménez Salazar
#Fecha de realización:21/04/2021 05:57 p.m.
#Última modificación:21/04/2021 11:11  p.m.
#Versión: 3.8.2

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

def validarLetras(texto):
    """
    Funcionamiento: Determina si es texto, sin caracteres especiales ni números, solo letras y espacios
    Entradas:
    -texto(string): La varaiable a validar 
    Salidas: 
    -True: Si es solo texto
    -False: En cualquier otro caso
    """
    lista = texto.split()
    for i in lista:
        if not i.isalpha():
            return False
    return True

def validarMurcielago(texto):
    lista = texto.split("*")
    for i in lista:
        if not i.isalnum():
            return False
    return True
def validarCenit(texto):
    lista = texto.split("¬")
    for i in lista:
        if not i.isalnum():
            return False
    return True
def validarDeletreoCifrar(texto):
    for i in texto:
        if not i.isalpha():
            return False
    return True
def validarDeletreoDescifrar(texto):
    lista = texto.split("~")
    for i in lista:
        if not i.isalpha():
            return False
    return True