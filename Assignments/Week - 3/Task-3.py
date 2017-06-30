def getCoordinates(turn, tt):
    player = ''
    while True:
        if turn % 2 == 0:
            inp = input("Player 1, enter your move in r,c format:")
            player = 'X'
        else:
            inp = input("Player 2, enter your move in r,c format:")
            player = 'O'

        inp = inp.split(',')
        inp = list(map(lambda a: int(a), inp))
        r = inp[0]-1
        c = inp[1]-1
        if tt[r][c] != -1:
            print('INVALID MOVE, TRY AGAIN!')
        else:
            break
    inp.append(player)
    return inp

def setCoordinates(t, m):
    m[0] -= 1
    m[1] -= 1
    t[m[0]][m[1]] = m[2]
    return t

def print_horiz_line():
    return '--- ' * 3

def print_vert_line():
    return '|'

def gameBoard(tt):
    ret = ''
    for i in range(3):
        for j in range(3):
            if j == 0:
                ret += print_horiz_line()
                ret += '\n'
            ret += print_vert_line()
            if tt[i][j] != -1:
                ret += tt[i][j]
            else:
                ret += ' '
            ret += print_vert_line()
            ret += ' '
        ret += '\n'
    ret += print_horiz_line()
    return ret

    print_horiz_line()
def main():
    tic_tac = list()
    for i in range(3):
        t = []
        for j in range(3):
            t.append(-1)
        tic_tac.append(t)
    #print(tic_tac)

    for i in range(9):
        g = getCoordinates(i, tic_tac)
        tic_tac = setCoordinates(tic_tac, g)
        #print(tic_tac)
        print(gameBoard(tic_tac))

if __name__ == "__main__":
    main()