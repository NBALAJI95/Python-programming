def checkAllLetters(s):
    alpha = []
    for l in s:
        if l not in alpha and l.isalpha():
            alpha.append(l)
    if len(alpha) == 26:
        return True
    else:
        return False


def main():
    inp_str = input('Enter the string:')
    if checkAllLetters(inp_str):
        print('The given string {0} contains all letters in english'.format(inp_str))
    else:
        print('The given string {0} does not contain all letters in english'.format(inp_str))

if __name__ == '__main__':
    main()