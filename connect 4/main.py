import ChessBoard

while True:
    player1 = 'player1'
    player2 = 'player2'
    turn = 0
    start = ChessBoard.FourInALine(6, 7)
    while True:
        p = player1 if turn % 2 == 0 else player2
        while True:
            print("Now {}'s turn, your icon is {}".format(p, start.getIcon(p)))
            num = input('Which column: ')
            if start.isValid(num):
                num = int(num)
                break
        result = start.putChess(p, num - 1)
        if result == 'FULL':
            print('Column {} is full. Choose another column!'.format(num))
        elif result == 'GAME DRAW':
            print('GAME DRAW!!')
            break
        elif type(result) == dict:
            print('Winner is {} {}'.format(result['winner'], start.getIcon(p)))
            break
        else:
            turn += 1
    if input('One more time?[y/n]: ') != 'y':
        print('Thanks for playing! Bye ~')
        break