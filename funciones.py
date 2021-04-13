
def procesarCodigoEucalipto(texto,opcion):

    eucalipto = ["E","U","C","A","L","I","P","T","O"]
    texto = texto.upper()
    resultado=""
    if opcion == 1: 
        for i in texto:
            if i in eucalipto:
                resultado+= str(eucalipto.index(i)+1)
            elif i == " ":
                resultado+= "°"
            else:
                resultado+= i
    else:
        for i in texto:
            if i.isdigit():
                resultado+= eucalipto[int(i)-1]
            elif i == "°":
                resultado+= " "
            else:
                resultado+= i
    return resultado
