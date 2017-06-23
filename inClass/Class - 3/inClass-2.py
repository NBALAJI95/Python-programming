
def cornerElements(l):
    return l[0] + ', ' + l[-1]


def main():
    n = input('Enter the input list separated by commas (,):')
    numbers = n.split(',')
    print(cornerElements(numbers))

if __name__ == '__main__':
    main()