def main():
    op = ''
    letter = [4, 2, 2, 2, 4]
    for i in range(5):
        for j in range(4):
            if i == 0 or i == 4:
                op += '* '
            elif i == 1 or i== 3:
                if j % 2 == 0:
                    op += '* '
                else:
                    op += ' '
            elif i == 2:
                if j == 0 or j == 1:
                    op += '* '
        op += '\n'
    print(op)

if __name__ == '__main__':
    main()