def findCharFreq(s, c):
    if c not in s:
        return 'Letter not in string'
    else:
        count = s.count(c)
        return count


def main():
    inp_str = input('Enter the string:')
    distinct_letters = []
    for i in inp_str:
        if i not in distinct_letters:
            distinct_letters.append(i)

    for e in distinct_letters:
        print('Character Frequency of %s is %s' % (e, findCharFreq(inp_str, e)))

if __name__ == '__main__':
    main()
