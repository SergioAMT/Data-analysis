import re

# hand = open('txt.txt')
# for line in hand:
#     line = line.rstrip()
#     # rstrip() remove any white spaces at the end of the string
#     if re.search('everyone', line):
#         print(line)
        
# la funcion re.search recorre la cadena
# de texto string buscando la primera coincidencia del 
# patrón pattern devolviendo el objeto match correspondiente. 
# En caso de no encontrarse ninguna coincidencia, la función devuelve None.   



secondPhrase = 'From: using the: character'
x = re.findall('^F.+:', secondPhrase)
print(x)

# phrase = 'my 2 favorite numbers are 19 and 42 and 2 '
# matching = re.findall('[0-9]+', phrase)
# print(matching)

a = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From \S+@\S+', a)
print(y)

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)

atpos = s.find('@')
sppos = s.find(' ', atpos)
host = s[atpos+1 : sppos]
print(host)

full = re.findall('@[^ ]*', s)
print(full)