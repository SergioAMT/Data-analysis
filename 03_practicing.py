# tax = 12.5 / 100
# price = 100.50
# price * tax
# 12.5625
# price + _
# 113.0625
# round(_, 2)
# 113.06
#En el modo interactivo, la última expresión impresa se asigna a la variable _. Esto significa que cuando se está utilizando Python como calculadora, es más fácil seguir calculando, por ejemplo:

word = 'akdkfefgjtjv'
print(len(word))

array = [1, 2, 3, 4, 5];
array2 = [6, 7, 8, 9 ,10];

arry3 = array + array2
print(arry3)

a, b = 0, 1;
while a < 10:
    print('El valor de a es ', a , '\nel valor de b es ', b)
    a, b = b, a+b
    
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active', 'bandipelos': 'inactive', 'ross': 'active'}

# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# print(users)

active_users = {}
for user, status in users.items():
    if status == 'inactive':
        active_users[user] = status

print(active_users)
print(type(active_users))
# for i in range(len(active_users)):
#     print (i, active_users)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
        
