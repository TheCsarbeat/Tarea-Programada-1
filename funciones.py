#no se códifican los espacios porque los acout no hablan en espacios espacios ocupan un letras leer
#Se mantien la robustez  ya que es la misma función codifica y decodifica, sin la necesecidad de pasar un paramentro o darle
#  más de una tarea a una funcion , sin segmentar la funcion en dos tareas 
from datetime import datetime
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
    print(caracteres)
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

def leerBitacora():
    try:
        bitacora = open("bitacora.txt","r")
        return True
    except:
        return False
def añadirBitacora(proceso,entrada,salida):
    ahora = datetime.now()
    if leerBitacora():
        bitacora = open("bitacora.txt","a")
        bitacora.write(+str(ahora.time())+" se ejecutó \t"+proceso+": entrada("+entrada+"), salida("+salida+")\n")

def crearBitacora():

    
    bitacora = open("Bitacora.txt","w")
    
    bitacora.close()