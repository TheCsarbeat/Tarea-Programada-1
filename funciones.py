#Creado por: César Jiménez Salazar
#Fecha de realización:14/04/2021 08:39 p.m.
#Última modificación:14/04/2021 03:39  p.m.
#Versión: 3.8.2
from datetime import datetime
def cifrarMurcielago(texto):
    """
    Funcionamiento: cifra el texto al código murciélago usado por los scouts
    Entradas: -texto: el texto a cifrar del usuario
    Salidas: retorna el texto cifrado en código murciélago
    """
    impresion = ""
    code = ["m","u","r","c","i","e","l","a","g","o"]
    for i in texto:
        if i in code:
            impresion+=str(code.index(i))
        elif i == " ":
            impresion+="*"
        else:
            impresion+=i
    return impresion
def descifrarMurcielago(texto):
    """
    Funcionamiento: descifra el texto en código muerciélago a su equivalente español
    Entradas: -texto: el texto a descifrar del usuario
    Salidas: retorna el texto descifrado del murciélago de entrada
    """
    impresion = ""
    texto = texto.lower()
    code = ["m","u","r","c","i","e","l","a","g","o"]
    for i in texto:
        if i.isdigit():
            impresion+=code[int(i)]
        elif i == "*":
            impresion+=" "
        else:
            impresion+=i
    return impresion
def cifrarCenitPolar(texto):
    """
    Funcionamiento: cifra el texto al cenit polar usado por los scouts, así como descifrarlo
    la razón por la que NO se dividen las tareas, es porque este código y la manera en que está
    programado permite que se le ingrese un texto cifrado y lo descifre sin necesidad de hacer
    ningún cambio mayor que implicase rigidez en el código
    Entradas: -texto: el texto a cifrar del usuario
    Salidas: retorna el texto cifrado en código cenit polar
    """
    impresion = ""
    texto = texto.lower()
    code = ["c","e","n","i","t","p","o","l","a","r"]
    for i in texto:
        if i in code:
            if code.index(i) < 5:
                impresion+=code[code.index(i)+5]
            else:
                impresion+=code[code.index(i)-5]
        elif i == " " or i == "¬":
            if i == " ":
                impresion+="¬"
            else:
                impresion+=" "
        else:
            impresion+=i
    return impresion
def cifrarDeletreo(texto):
    """
    Funcionamiento: cifra el texto en código deletreo
    Entradas: -texto: el texto a cifrar del usuario
    Salidas: retorna el texto cifrado en codigo deletreo
    """
    impresion = ""
    texto = texto.lower()
    code = ["alfa","bravo","charlie","delta","echo","foxtrot","golf","hotel","india","juliet","kilo","lima","mike","november","oscar",\
        "papa","quebec","romeo","sierra","tango","uniform","victor","whisky","xray","yanqui","zulú"]
    for i in texto:
        for j in code:
            if i == j[0]:
                impresion+=j
                impresion+="~"
    impresion = limpiarUltimoCaracter(impresion)
    return impresion
def descifrarDeletreo(texto):
    """
    Funcionamiento: descifra el texto del código deletreo al español
    Entradas: -texto: el texto a cifrar del usuario
    Salidas: retorna el texto descifrado del código deletreo
    """
    impresion = ""
    code = texto.lower().split("~")
    for i in code:
        if not i == "":
            impresion+=i[0]
    return impresion
def cifrarEucalipto(texto):
    """
    Funcionamiento: Encripta el texto ingresado en código eucalipto
    Entradas:
    -texto(string): El texto a encriptar
    Salidas: 
    -resultado(string): El texto encriptado
    """
    eucalipto = ["e","u","c","a","l","i","p","t","o"]
    texto = texto.lower()
    resultado=""
    for i in texto:
        if i in eucalipto:
            resultado+= str(eucalipto.index(i)+1)
        elif i == " ":
            resultado+= "°"
        else:
            resultado+= i
    return resultado

def descifrarEucalipto(texto):
    """
    Funcionamiento: Desencripta el texto ingresado en código eucalipto
    Entradas:
    -texto(string): El texto a desencriptar
    Salidas: 
    -resultado(string): El texto desencriptar
    """
    eucalipto = ["e","u","c","a","l","i","p","t","o"]
    texto = texto.lower()
    resultado=""
    for i in texto:
        if i.isdigit():
            resultado+= eucalipto[int(i)-1]
        elif i == "°":
            resultado+= " "
        else:
            resultado+= i    
    return resultado

def cifrarMorse(texto):
    """
    Funcionamiento: Encripta el texto ingresado en código morse
    Entradas:
    -texto(string): El texto a encriptar
    Salidas: 
    -resultado(string): El texto encriptado
    """
    morse = [".-", "-...", "-.-.","-..", ".","..-.","--.","....", "..","·---","-.-",".-..","--", "-.", "--.--", "---",".--.","--.-",".-.", "...",\
    "-","..-","...-",".--","-..-","-.--","--..",  "-----", ".----", "..---", "...--", "....-",".....", "-....", "--...", "---..", "----.",]
    alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    texto = texto.lower()
    resultado=""
    for i in texto:
        if i in alfabeto:
            resultado+= str(morse[alfabeto.index(i)])+"^"
        else:
            resultado = limpiarUltimoCaracter(resultado)
            resultado+= "|"
    resultado = limpiarUltimoCaracter(resultado)
    return resultado

def descifrarMorse(texto):
    """
    Funcionamiento: Encripta el texto ingresado en código morse
    Entradas:
    -texto(string): El texto a encriptar
    Salidas: 
    -resultado(string): El texto encriptado
    """
    morse = [".-", "-...", "-.-.","-..", ".","..-.","--.","....", "..",".---","-.-",".-..","--", "-.","---",".--.","--.-",".-.", "...",\
    "-","..-","...-",".--","-..-","-.--","--..",  "-----", ".----", "..---", "...--", "....-",".....", "-....", "--...", "---..", "----.",]
    alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    texto = texto.lower()
    resultado=""
    caracteres = texto.split("^")
    for i in caracteres:
        if i in morse:
            resultado+= str(alfabeto[morse.index(i)])
        elif "|" in i: 
            for j in i.split("|"):
                if j in morse :
                    resultado+= str(alfabeto[morse.index(j)])+" "
                elif j != "": # no sirve hacer un else solo ya que lo que se queire es olo no esta en los códigos morse que imprima un caracter in vlálido
                    resultado += "?"
            resultado = limpiarUltimoCaracter(resultado)
        elif i != "": # no sirve hacer un else solo ya que lo que se queire es olo no esta en los códigos morse que imprima un caracter in vlálido
            resultado += "?"
    return resultado

def determinarPar(num):
    """
    Funcionamiento: Determina si el número es par
    Entradas:
    -num(int): número a válidar
    Salidas: 
    -True: si es par
    -False: si no es par
    """
    if num % 2 ==0:
        return True
    else:
        return False

def codigoSufamelico(texto):
    """
    Funcionamiento: cifra el texto al sufamelico usado por los scouts, así como descifrarlo
    la razón por la que NO se dividen las tareas, es porque este código y la manera en que está
    programado permite que se le ingrese un texto cifrado y lo descifre sin necesidad de hacer
    ningún cambio mayor que implicase rigidez en el código
    Entradas: 
    -texto: el texto a cifrar del usuario
    Salidas:
    -retorna el texto cifrado en código cenit polar
    """
    impresion = ""
    texto = texto.lower()
    code = ["s","u","f","a","m","e","l","i","c","o"]
    for i in texto:
        if i in code:
            if determinarPar(code.index(i)):
                impresion+=code[code.index(i)+1]
            else:
                impresion+=code[code.index(i)-1]
        else:
            impresion+=i
    return impresion

def limpiarUltimoCaracter(texto):
    """
    Funcionamiento: Se encarga de eliminar el último caracter de una cadena de texto
    Entradas: 
    -texto(string): la variable a utilizar
    Salidas:
    -retorna el texto sin el último caracter
    """
    return texto[:len(texto)-1]

def buscarBitacora():
    """
    Funcionamiento: Determina si el archiv de bitácora existe.
    Entradas: 
    -NA
    Salidas:
    -True: si el archivo existe
    -False: si no existe
    """       
    try:
        bitacora = open("Bitácora.txt","r")
        bitacora.close()
        return True
    except:
        return False
        
def añadirBitacora(proceso,entrada,salida):
    """
    Funcionamiento: Agrega al archivo bitacora un nuevo registro.
    Entradas: 
    -proceso(string): El nombre del proceso que se ejecutó
    -entrada(string): La entrada que recibió el procesos ejecutado.
    -salida(string): La respuesta del proceso ejecutado.
    Salidas:
    -Una nueva línea en el archivo de bitácora.
    """       
    now = datetime.now()
    if buscarBitacora():
        bitacora = open("Bitácora.txt","a")
        bitacora.write(now.strftime("%H:%M:%S")+"\t"+proceso+": entrada("+entrada+"), salida("+salida+")\n")
        bitacora.close()
    else:
        crearBitacora()
        añadirBitacora(proceso,entrada,salida)
    return ""

def crearBitacora():
    """
    Funcionamiento: Crea el archivo de texto bitácora.
    Entradas: 
    -NA
    Salidas:
    -Un arcivho tipo txt llamado bitácora.
    """       
    bitacora = open("Bitácora.txt","w")
    bitacora.close()
    return"" 