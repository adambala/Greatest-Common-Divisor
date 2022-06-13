from random import randint


def gcd(a, b):
    """
    Euclidean algorithm for the highest common factor of two integers.

    Return the greatest common divisor of a and b
    """
    if (a != 0) and (b != 0):
        if a > b:
            return gcd(a % b, b)
        else:
            return gcd(a, b % a)
    else:
        return a + b


def testGCD(rangeBoundary=1000, testNumber=100):
    """
    Takes two random integers several times and calculates gcd.

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
        mSpaces = ' '*(len(str(rangeBoundary)) - (len(str(m)) + 1))
        nSpaces = ' '*(len(str(rangeBoundary)) - (len(str(n)) + 1))
        print(f'm = {m}' + mSpaces, end=' || ')
        print(f'n = {n}' + nSpaces, end=' || ')
        print(f'gcd(m, n) = {result}')


if __name__ == "__main__":
    testGCD(rangeBoundary=10000, testNumber=10)
