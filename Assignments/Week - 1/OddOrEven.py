def checkOddOrEven(n):
	# if reminder is 0 after dividing by 2 it's even
    if n % 2 == 0:
        return "Number entered by user is even"
    else:
	# else it is odd
        return "Number entered by user is odd"

def main():
	# Get a number as input
    num = int(input("Enter Number:"))
    print(checkOddOrEven(num))

if __name__ == '__main__':
    main()