# Nathan Maurer
# January 11, 2025
# Module 1_3 Assignment
# Advanced Python

def main():
    # defines end of program once i=0
    def sing(a, end):
        print (a or 'Time to buy more','bottle'+('s' if a-1 else ''), end)

    # user entered data
    number = int(input('How many beers do we start with? '))

    # loop using range, this range is defined by the user
    for i in range (number,0,-1):
        sing(i, 'of beer on the wall,')
        sing(i, 'of beer,')
        print('Take one down, pass it around,')
        sing(i-1, 'of beer on the wall.\n')

if __name__ == '__main__':
    main()