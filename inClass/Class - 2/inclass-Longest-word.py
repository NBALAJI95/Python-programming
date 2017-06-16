def findLongest(l):
    max_v = -1
    max_str = str()
    for i in l:
        if len(i) > max_v:
            max_v = len(i)
            max_str = i
    return 'Length of longest string %s in the list is %d' % (max_str, max_v)


def main():
    inp_list = list()
    while True:
        if input('Are you done adding words to the list? \n Y - yes: ').lower() == 'y':
            break
        else:
            inp_list.append(input('Enter word to insert: '))
    print('\nList of input of words', inp_list)
    print(findLongest(inp_list))

if __name__ == '__main__':
    main()