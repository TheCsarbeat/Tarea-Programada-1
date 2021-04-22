#Creado por: César Jiménez Salazar
#Fecha de realización:14/04/2021 08:39 p.m.
#Última modificación:14/04/2021 03:39  p.m.
#Versión: 3.8.2

def cifrarMurcielago(texto):
    """
    Funcionamiento: cifra el texto al código murciélago usado por los scouts
    Entradas: -texto: el texto a cifrar del usuario
    Salidas: retorna el texto cifrado en código murciélago
    """
    impresion = ""
    texto = texto.lower()
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
                if not i == texto[-1]: #esto es para que cuando llegue a la ultima posicion no vuelva a agregar ~
                    impresion+="~"
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
        impresion+=i[0]
    return impresion