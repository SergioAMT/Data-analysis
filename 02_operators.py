# Operators
print(3 + 4, 3 / 4)
print(10 // 3)#floor division aproxima el valor

astr = 'hello sergio'
try:
    istr = int(astr)
except:
    istr = -1
print ('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)

def thing():
    print('hello')
    print('fun')
    
thing()
print('zip')
thing()

big = max('Hello word')
print(big)
type(big)