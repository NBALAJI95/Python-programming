def checkOddOrEven(n):
    if n % 2 == 0:
        return "Number entered by user is even"
    else:
        return "Number entered by user is odd"

def main():
    num = int(input("Enter Number:"))
    print(checkOddOrEven(num))

if __name__ == '__main__':
    main()