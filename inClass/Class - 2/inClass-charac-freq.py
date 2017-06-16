def findCharFreq(s, c):
    if c not in s:
        return 'Letter not in string'
    else:
        count = s.count(c)
        return str(count / len(s) * 100)+'%'


def main():
    inp_str = input('Enter the string:')
    char = input('Enter a letter in the string:')
    print('Character Frequency', findCharFreq(inp_str, char))

if __name__ == '__main__':
    main()
