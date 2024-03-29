from random import randint
from gcd import gcd
from math import log10


def intInput(inputText='') -> int:
    """
    Uses built-in input() function and return an int value of input string.

    If input string cannot be turned into an integer the function will ask user to write it again.

    Parameters:
        inputText: String used for input() function
    """
    while True:
        try:
            returnValue = int(input(inputText))
        except ValueError:
            print("Input must be an integer value!")
            continue

        return returnValue


def testGCD(rangeBoundary, testNumber):
    """
    Takes two random integers several times and calculates their greatest common divisor.

    Prints the result to the console.

    Parameters:
        rangeBoundary: maximum possible generated integer
        testNumber:    the number of tests to be calculated.
    """
    digit_number = int(log10(rangeBoundary)) + 1
    for i in range(testNumber):
        m = randint(1, abs(rangeBoundary))  # abs() used to avoid errors with negative numbers
        n = randint(1, abs(rangeBoundary))
        result = gcd(m, n)

        # output

        print(f'{m = : <{digit_number}}', end=' || ')
        print(f'{n = : <{digit_number}}', end=' || ')
        print(f'gcd(m, n) = {result}')


if __name__ == "__main__":
    rB = intInput("Maximum possible integer: ")
    tN = intInput("Number of tests: ")
    testGCD(rangeBoundary=rB, testNumber=tN)
