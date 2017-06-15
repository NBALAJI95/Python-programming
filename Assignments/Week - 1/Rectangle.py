def perimeter_Rectangle(l, b):
	# finding perimeter of a rectangle: 2 times length times breadth
    return 2 * (l + b)

def area_Rectangle(l, b):
	# finding area of rectangle: length times breadth
    return l * b

def main():
	# Get length and breadth as input
    length = int(input("Enter length:"))
    breadth = int(input("Enter breadth:"))
	# print the final values
    print('Perimeter of the rectangle with length', length, 'and', 'breadth', breadth , 'is',perimeter_Rectangle(length, breadth))
    print('Area of the rectangle with length', length, 'and', 'breadth', breadth , 'is',area_Rectangle(length, breadth))

if __name__ == '__main__':
    main()