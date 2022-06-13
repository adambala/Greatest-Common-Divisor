# Greatest common divisor
GCD is the mathematical problem of finding the highest common factor of two non-zero integers.

This program uses [Euclidian algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) to find GCD of two integers.

## GCD function
The `gcd(a, b)` function returns the greatest common divisor of its two integer arguments `a` and `b`.

### Example
```python
gcd(48, 18)
# 6
```

## Tests
The program has `testGCD` function which takes two random integers `m` and `n` via `random` library for several times and calculates `gcd(m, n)`.
It is being used in order to demonstrate the accuracy of `gcd(a, b)`.

The function has two optional keyword arguments:
1. `rangeBoundary`: maximum possible generated integer,
2. `testNumber`: the number of tests to be calculated.

###In program:
```python
testGCD(rangeBoundary=10000, testNumber=10)
```

###Output example:
```
m = 622  || n = 8119 || gcd(m, n) = 1
m = 9497 || n = 257  || gcd(m, n) = 1
m = 2146 || n = 7985 || gcd(m, n) = 1
m = 1789 || n = 8731 || gcd(m, n) = 1
m = 640  || n = 2256 || gcd(m, n) = 16
m = 3008 || n = 1224 || gcd(m, n) = 8
m = 68   || n = 440  || gcd(m, n) = 4
m = 7076 || n = 1097 || gcd(m, n) = 1
m = 7431 || n = 1753 || gcd(m, n) = 1
m = 5377 || n = 4267 || gcd(m, n) = 1
```