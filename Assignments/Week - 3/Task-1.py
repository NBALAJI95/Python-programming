def main():
    # Getting input string and making it into list & tuples
    # Exception handling does not make any sense in this case
    inp = input('Enter a string:')
    print(list(inp))
    print(tuple(inp))

if __name__ == '__main__':
    main()