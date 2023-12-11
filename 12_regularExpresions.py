import re

hand = open('txt.txt')
for line in hand:
    line = line.rstrip()
    # rstrip() remove any white spaces at the end of the string
    if re.search('everyone', line):
        print(line)
        
# la funcion re.search recorre la cadena
# de texto string buscando la primera coincidencia del 
# patrón pattern devolviendo el objeto match correspondiente. 
# En caso de no encontrarse ninguna coincidencia, la función devuelve None.       