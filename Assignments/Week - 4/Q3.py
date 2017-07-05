def main():
    input_list = input('Input:')
    # Splitting input by comma
    input_list = input_list.split(',')
    # Sorting the list
    input_list.sort()
    output_list = input_list
    print(output_list)

if __name__ == '__main__':
    main()
