#Creado por: César Jiménez Salazar, Maynor Martínez
#Fecha de realización: 14/04/2021 06:00 p.m.
#Última modificación: 29/04/2021 11:43  p.m.
#Versión: 3.9.2
#----------------------------------------------------------------------#
#                         VALIDACIONES GENERALES                       #
#----------------------------------------------------------------------#
def validarVacio(texto):
    """
    Funcionamiento: Determina si la variable es vacía
    Entradas:
    -texto(string): la variable a validar 
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
    Funcionamiento: Determina si es texto, sin caracteres especiales ni números, solo letras, espacios,
    comas, y puntos.
    Entradas:
    -texto(string): La variable a validar 
    Salidas: 
    -True: Si es solo texto, (,) o (.)
    -False: En cualquier otro caso
    """
    for i in texto:
        if (i.isalpha()== False) and not(i in ",. "):
            return False
    return True
def validarEntero(num):
    """
    Funcionamiento: Determina si el número es connveritble a  un entero
    Entradas:
    -num(string): Una cadena de texto con la posibilidad de ser entero
    Salidas: 
    -True si el número sí es entero
    -False si el número no fuese entero. 
    """
    try:
        num = int(num)
        if num > 0:
            return True
    except ValueError:
        return False
#----------------------------------------------------------------------#
#                  VALIDACIONES DE PROCESAMIENTO                       #
#----------------------------------------------------------------------#
def validarMurcielago(texto):
    """
    Funcionamiento: Determina si es texto, letras, numeros, asteriscos, comas, y puntos.
    Entradas:
    -texto(string): La variable a validar
    Salidas: 
    -True: si contiene unicamente letras, numeros, asteriscos, comas, y puntos.
    -False: En cualquier otro caso
    """
    for i in texto:
        if (i.isalnum()== False) and not(i in ",.*"):
            return False
    return True
def validarCenit(texto):
    """
    Funcionamiento: Determina si es texto, letras, (¬), comas, y puntos.
    Entradas:
    -texto(string): La variable a validar
    Salidas: 
    -True: si contiene unicamente letras, (¬), comas, y puntos.
    -False: En cualquier otro caso
    """
    for i in texto:
        if (i.isalpha()== False) and not(i in ",.¬"):
            return False
    return True
def validarDeletreoCifrar(texto):
    """
    Funcionamiento: Determina si solo contiene letras
    Entradas:
    -texto(string): La variable a validar
    Salidas: 
    -True: si contiene unicamente letras
    -False: En cualquier otro caso
    """
    for i in texto:
        if not i.isalpha():
            return False
    return True
def validarDeletreoDescifrar(texto):
    """
    Funcionamiento: Determina si solo contiene letras
    Entradas:
    -texto(string): La variable a validar
    Salidas: 
    -True: si contiene unicamente letras o (~)
    -False: En cualquier otro caso
    """
    for i in texto:
        if (i.isalpha()== False) and not(i == "~"):
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