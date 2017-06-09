def perimeter_Rectangle(l, b):
    return 2 * (l + b)

def area_Rectangle(l, b):
    return l * b

def main():
    length = int(input("Enter length:"))
    breadth = int(input("Enter breadth:"))
    print('Perimeter of the rectangle with length', length, 'and', 'breadth', breadth , 'is',perimeter_Rectangle(length, breadth))
    print('Area of the rectangle with length', length, 'and', 'breadth', breadth , 'is',area_Rectangle(length, breadth))

if __name__ == '__main__':
    main()