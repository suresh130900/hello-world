def print_input(inputs):
    print(inputs[7]+ '|' +inputs[8]+ '|' +inputs[9])
    print('- - -')
    print(inputs[4]+ '|' +inputs[5]+ '|' +inputs[6])
    print('- - -')
    print(inputs[1]+ '|' +inputs[2]+ '|' +inputs[3])

def check_win(inputs):
    #horizontal
    game=' '
    while game!='win':
        num1 = int(input('Player1, Enter a number between (1-9): '))
        inputs[num1] = 'x'
        print_input(inputs)
        if inputs[1]==inputs[2]==inputs[3]==player1:
            print('Player1, Won the match.')
            game = 'win'
            break

        elif (inputs[1]==inputs[2]==inputs[3]==player2):
            print('Player2, Won the match.')
            game = 'win'
            break
    
        elif(inputs[4]==inputs[5]==inputs[6]==player1):
            print('Player1, Won the match')
            game = 'win'
            break
    
        elif(inputs[4]==inputs[5]==inputs[6]==player2):
            print('Player2, Won the match')
            game = 'win'
            break
    
        elif(inputs[7]==inputs[8]==inputs[9]==player1):
            print('You Won the match.')
            game = 'win'
            break

    #vertical wining condition
        elif(inputs[1]==inputs[4]==inputs[7]==player1):
            print('You Won the match.')
            game = 'win'
            break

        elif(inputs[2]==inputs[5]==inputs[8]==player1):
            print('You Won the game')
            game = 'win'
            break
                
        elif(inputs[3]==inputs[6]==inputs[9]==player1):
            print('You Won the match.')
            game = 'win'
            break

    #diagonal wining condition
        elif(inputs[1]==inputs[5]==inputs[9]==player1):
            print('You Won the match.')
            game = 'win'
            break
            
        elif(inputs[3]==inputs[5]==inputs[7]==player1):
            print('You Won the match.')
            game = 'win'
            break

    #draw condition
        elif(inputs[1]!=' ' and inputs[2]!=' ' and inputs[3]!=' ' and inputs[4]!=' ' and inputs[5]!=' ' and inputs[6]!=' ' and inputs[7]!=' ' and inputs[8]!=' ' and inputs[9]!=' '):
            print('Draw')
            game = 'win'
            break
            
        else:
            pass

        num2 = int(input('Player2, Enter a number between (1-9): '))
        inputs[num2] = 'o'
        print_input(inputs)
    
print('Welcome To Tic-Tac-Toe Game.')
player1=' '
player2=' '
inputs = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
while player1 !='x' and player1 !='o':
    player1 = input('Player1, choose X or O:')

if player1 == 'x':
    player2 = 'o'
else:
    player2 = 'x'
print('Player1 will have '+player1)
print('Player2 will have '+player2)
check_win(inputs)
