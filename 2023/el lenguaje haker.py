"""
Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 *  Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *  con el alfabeto y los números en "leet".
 *  (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
""" 

def convertidorMinus(texto):
    textominus = texto.lower()
    return textominus


def crearListaLetras(textominus):
    textolistletras = list(textominus)
    return textolistletras

def traducirTexto(textolistletras):
    finaldict = dict()
    #textolistletra = len(textolistletras)
    leetD = len(leetDict)
    print(texto)
    x = 0
    for letra in textolistletras:
        for signo in leetDict:
            if signo == letra:
                leet.append(signo)
                print(letra, leetDict[signo])
                finaldict[letra] = leetDict[signo]
                x += 1
                if x == leetD:
                    print(finaldict)
                break
        
     
texto = ("Hace dos horas, cuando todo comenzo, la gente no gritaba\
Nadie levantaba los puños, ni cerraba los ojos, ni miraba el escenario\
con arrobo. Hace dos horas todos hacian un ensayo general de histeria de\
bajo voltaje alla en la calle, cuando ellos cinco gafas oscuras, pantalones\
de cuero bajaban de la limusina alquilada, polarizada, vieja, entre el humo\
de los chorizos que se asaban en los puestos callejeros. Hace dos horas, cuando\
todo comenzo, la gente aplaudia un poco, y nada mas. La gente gritaba un poco, y nada\
mas. La gente bailaba un poco, y nada mas")

leetDict = {
    "a":"4",
    "b":"I3",
    "c":"[",
    "d":")",
    "e":"3",
    "f":"|=",
    "g":"&",
    "h":"#",
    "i":"1",
    "j":",_|",
    "k":">|",
    "l":"£",
    "m":"/\/\\",
    "n":"^/",
    "o":"0",
    "p":"|*",
    "q":"(_,)",
    "r":"I2",
    "s":"5",
    "t":"7",
    "u":"(_)",
    "v":"\\/",
    "w":"\\_:_/",
    "x":"><",
    "y":"j",
    "z":"2"
}

leet = []


textominus = convertidorMinus(texto)

textolistletras = crearListaLetras(textominus)

traduccion = traducirTexto(textolistletras)