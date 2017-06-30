
def main():
    inp = input('Enter numbers, tuples separated by ";":')
    try:
        inp = inp.split(';')
        inp = list(filter(lambda a: a!='', inp))

        inp = list(map(lambda a: a.split(','), inp))
    except:
        print('Invalid input!\nBetter luck next time')

    inp1 = list()
    for i in inp:
        inp1.append(tuple(map(lambda a: int(a), i)))
    print(inp1)

    inp1 = sorted(inp1, key = lambda a: a[1])
    print(inp1)


if __name__ == '__main__':
    main()