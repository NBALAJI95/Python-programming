from math import pi

def area(rad):
    return pi * (rad ** 2)

def circumference(rad):
    return 2 * pi * rad

def main():
    r = int(input("Enter radius:"))
    print("Area of the circle is", area(r))
    print("Circumference of the circle is", circumference(r))

if __name__ == '__main__':
    main()