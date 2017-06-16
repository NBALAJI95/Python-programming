def findDigitsLetters(s):
    digit = 0
    alpha = 0
    for c in s:
        if c.isdigit():
            digit += 1
        elif c.isalpha():
            alpha += 1
    return {'Digit': digit, 'Alpha': alpha}


def main():
    inp_str = input('Enter input string:')
    result = findDigitsLetters(inp_str)
    print('Number of digits in the string', result['Digit'])
    print('Number of alphabets in the string', result['Alpha'])

if __name__ == '__main__':
    main()
