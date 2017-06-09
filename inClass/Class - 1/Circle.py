'''
Differences between Python 2 and Python 3?
1. Input
Python 2: raw_input()
Python 3: input()

2. Print
Python 2: print ‘Statement‘
Python 3: print(‘Statement’)

3. Default Division
Python 2: 7 / 2 # ---> 3
Python 3: 7 / 2 # ---> 3.5
'''

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