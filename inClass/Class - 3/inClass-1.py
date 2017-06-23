
def print_horiz_line():
    return '---'

def print_vert_line():
    return '|'

def main():
    inp = input('Enter dimensions of the board separated by "x":')
    inp = inp.split('x')
    inp = list(map(lambda a: int(a), inp))
    print(inp)
    op =''
    t = 0
    case = ''
    it = 0

    if (inp[0] + inp[1]) % 2 == 0:
        it = inp[0] + inp[1] + 1
    else:
        it = inp[0] + inp[1]

    for i in range(it):
        if i % 2 == 0:
            t = inp[1]
            case = 'even'
        else:
            t = inp[1] + 1
            case = 'odd'
        for j in range(t):
            if j == 0 and case == 'even':
                op += ' '
            if case == 'even':
                op += print_horiz_line() + ' '
            elif case == 'odd':
                op += print_vert_line()
                op += '   '
        op += '\n'
    print(op)

if __name__ == '__main__':
    main()