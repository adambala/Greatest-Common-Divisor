from random import randint

from gcd import gcd


def testGCD(rangeBoundary, testNumber):
    """
    Takes two random integers several times and calculates their greatest common divisor.

    Prints the result to the console.

    Optional keyword arguments:
    - rangeBoundary: maximum possible generated integer
    - testNumber:    the number of tests to be calculated.
    """
    for i in range(testNumber):
        m = randint(0, rangeBoundary)
        n = randint(0, rangeBoundary)
        result = gcd(m, n)

        # output

        print(f'm = {m}', end=' || ')
        print(f'n = {n}', end=' || ')
        print(f'gcd(m, n) = {result}')


if __name__ == "__main__":
    rB = int(input("Maximum possible integer: "))
    tN = int(input("Number of tests: "))
    testGCD(rangeBoundary=rB, testNumber=tN)
