from random import randint


def gcd(a, b):
    """
    Return the highest common factor of two non-zero integers.

    Calculates the greatest common divisor via Euclidian algorithm.
    """
    if (a != 0) and (b != 0):
        if a > b:
            return gcd(a % b, b)
        else:
            return gcd(a, b % a)
    else:
        return a + b


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
        mSpaces = ' '*(len(str(rangeBoundary)) - (len(str(m)) + 1))
        nSpaces = ' '*(len(str(rangeBoundary)) - (len(str(n)) + 1))
        print(f'm = {m}' + mSpaces, end=' || ')
        print(f'n = {n}' + nSpaces, end=' || ')
        print(f'gcd(m, n) = {result}')


if __name__ == "__main__":
    rB = int(input("Maximum possible integer: "))
    tN = int(input("Number of tests: "))
    testGCD(rangeBoundary=rB, testNumber=tN)
