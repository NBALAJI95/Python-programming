def main():
    # Inputting Set 1 values
    i_p_1 = input('Set 1 elements separated by comma:')
    i_p_1 = i_p_1.split(',')

    # Inputting Set 2 values
    i_p_2 = input('Set 2 elements separated by comma:')
    i_p_2 = i_p_2.split(',')

    set1 = set()
    set2 = set()

    # Creating set 1
    for i in i_p_1:
        if i.isdigit():
            i = int(i)
        set1.add(i)

    # Creating set 2
    for i in i_p_2:
        if i.isdigit():
            i = int(i)
        set2.add(i)

    # Displaying symmetric difference
    print(set1 ^ set2)

if __name__ == '__main__':
    main()
