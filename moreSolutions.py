# Contar cuantas veces se repite cada palabra dada una string

def tooLowerCase(texto):
    """convertir a minusculas 

    Args:
        text (String): cadena de texto inicial
    Returns:
        String: cadena en minusculas
    """
    lowerCase = texto.lower()
    return lowerCase


def cleanString(textLower):
    """
    Args:
        textLower: String
    Returns:
        Array = cadena de texto limpia
    """
    cleanedText = textLower.replace(',', '').replace('.', '')
    textoSeparado = cleanedText.split(" ")
    return textoSeparado

def countWords(cleanText):
    """
    Contador de cuantas palabras hay en la string
    Args:
        cleanText: list

    Returns:
        Dictionary : cantidad
    """
    dictionary = {}
    for word in cleanText:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return  dictionary

text = "Buenas noches caballero, le invito a pasar la noche conmigo porque usted es una persona ideal para esta velada y usted es algo amable."

lowerCase = tooLowerCase(text)
cleanTexted = cleanString(lowerCase)
contador = countWords(cleanTexted)
print(contador)