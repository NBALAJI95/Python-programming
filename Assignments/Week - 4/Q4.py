def main():
    i_p_1 = input('Set 1 elements separated by comma:')
    i_p_1 = i_p_1.split(',')

    i_p_2 = input('Set 2 elements separated by comma:')
    i_p_2 = i_p_2.split(',')

    set1 = set()
    set2 = set()

    for i in i_p_1:
        if i.isdigit():
            i = int(i)
        set1.add(i)

    for i in i_p_2:
        if i.isdigit():
            i = int(i)
        set2.add(i)

    print(set1 ^ set2)

if __name__ == '__main__':
    main()
