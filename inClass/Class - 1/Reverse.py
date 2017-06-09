def rev(n):
    rev = 0
    mul = 10 ** (len(str(n))-1)
    while n > 0:
        rem = n % 10
        rev += rem * mul
        mul = mul//10
        n = n//10
    return rev

def main():
    num = int(input("Enter a number:"))
    print("Reverse of the number is", rev(num))

if __name__ == '__main__':
    main()