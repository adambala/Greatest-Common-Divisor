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

