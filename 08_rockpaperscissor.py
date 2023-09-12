import random

options = ('rock', 'paper', 'scissors')
victories = 0

running = True
while running:
    
    computer = random.choice(options)
    player = None
    while player not in options:
        player = input('Enter a choise (rock, paper, scissors): ')

    print(f"player: {player}")
    print(f'computer: {computer}') 

    if player == computer:
        print('It is a tie')
    elif (player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock'):
        print('you win')
        victories += 1
        print (victories)
    else:
        print ('computer win')
        
    
    if not input ('Play again? (y/n)').lower() == 'y':
        running = False
        
print('thanks for playing')