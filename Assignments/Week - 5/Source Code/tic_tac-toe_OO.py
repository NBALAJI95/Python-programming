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
        r = inp[0] - 1
        c = inp[1] - 1
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


class Game:
    def __init__(self, r=3, c=3):
        self.row = r
        self.col = c
        self.tic_tac = list()

    def build(self):
        for i in range(self.row):
            t = []
            for j in range(self.col):
                t.append(-1)
            self.tic_tac.append(t)

    def forward_cross(self):
        cond = None
        for i in range(self.row):
            for j in range(self.col):
                if i != self.row - 1 and j != self.col - 1:
                    if i == j:
                        if self.tic_tac[i][j] == self.tic_tac[i+1][j + 1] and self.tic_tac[i][j] != -1:
                            cond = True
                        else:
                            cond = False
                            break
        if cond:
            return cond
        return cond

    def check_vertical(self):
        for i in range(self.col):
            cond = None
            for j in range(self.row):
                if j != self.row - 1:
                    if self.tic_tac[j][i] == self.tic_tac[j+1][i] and self.tic_tac[j][i] != -1:
                        cond = True
                    else:
                        cond = False
                        break
            if cond:
                return cond
        return cond

    def check_horizontal(self):
        for i in range(self.row):
            cond = None
            for j in range(self.col):
                if j != self.col-1:
                    #print('comp', self.tic_tac[i][j], self.tic_tac[i][j + 1])
                    if self.tic_tac[i][j] == self.tic_tac[i][j+1] and self.tic_tac[i][j] != -1:
                        cond = True
                    else:
                        cond = False
                        break
            if cond:
                return cond
        #print('cond',cond)
        return cond

    def reverse_cross(self):
        cond = None
        for i in list(reversed(range(self.row))):
            for j in range(self.col):
                if i != 0 and j != self.col:
                    if i + j == 2:
                        #print('i,j', i, j)
                        #print('comp', self.tic_tac[i][j], self.tic_tac[i - 1][j + 1])
                        if self.tic_tac[i][j] == self.tic_tac[i - 1][j + 1] and self.tic_tac[i][j] != -1:
                            #print('True')
                            cond = True
                        else:
                            cond = False
                            return cond
                            #print('i,j', i, j)
                            break
        if cond:
            return cond
        return cond

    def check_winning_condition(self):
        if self.check_horizontal():
            return True

        elif self.check_vertical():
            return True

        elif self.forward_cross():
            return True

        elif self.reverse_cross():
            return True

        else:
            return False


    def play(self):
        for i in range(self.row * self.col):
            g = getCoordinates(i, self.tic_tac)
            self.tic_tac = setCoordinates(self.tic_tac, g)
            print(gameBoard(self.tic_tac))
            if self.check_winning_condition():
                print('*************')
                print(g[2],'wins!!!!')
                break


def main():
    new_game = Game()
    new_game.build()
    new_game.play()

if __name__ == "__main__":
    main()