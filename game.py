from class_game import Game
n , k = int(input('Enter the field size: ')) , int(input('Enter K = '))
mode = int(input( 'Select the game mode:\n 1) 2 players : '))
mode = 1
current_game = Game(n , k , mode)
for i in range(n * n):
    if(current_game.move() == None):
        continue
    else:
        break
if(current_game.result == 0):
    print('Draw')
elif(current_game.result == 1):
    print('First player won!')
else:
    print('Second player won!')
