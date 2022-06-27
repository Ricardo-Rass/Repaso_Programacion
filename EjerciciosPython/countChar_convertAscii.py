#EJERCICIO:cuenta characteres duplicados y convierte a ASCII

#funcion que convierte a ascii
def toAscii(character):
    a=character.encode()[0]
    return a

#funcion que cuenta duplicados
def contar(text):
    #diccionario vacio que guardara las cosas 
    dic={}
    #limpia el texto quitando comas, puntos y espacios
    textoLimpio=text.lower().replace(",","").replace(".","").replace(" ","")
    #itera el texto ya limpio
    for a in textoLimpio:
        #The keys() method returns a view object that displays a list of all the keys in the dictionary
        llaves = dic.keys()
        #si no esta duplicado pon 1
        if a not in llaves:
            dic[a] = 1
        #si si esta duplicado suma 1    
        else:
            dic[a] += 1

    return dic                  
     
     
print(contar("holaa ")) 
print(toAscii("a"))