# Greatest common divisor
GCD is the mathematical problem of finding the highest common factor of two non-zero integers.

This program uses [Euclidian algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) to find GCD of two integers.

## GCD function
The `gcd(a, b)` function returns the greatest common divisor of its two integer arguments `a` and `b`.

### Example
```python
gcd(48, 18) # 6
```

## Tests
`test.py` file has `testGCD` function which takes two random integers `m` and `n` via `random` library for several times and calculates `gcd(m, n)`.
It is used to demonstrate the efficiency of `gcd(a, b)`.

The function has two keyword arguments:
1. `rangeBoundary`: maximum possible generated integer,
2. `testNumber`: the number of tests to be calculated.

The program takes these values from input.

### Input example:
```
Maximum possible integer: 10000
Number of tests: 10
```

### Output example:
```
m = 9444 || n = 3789 || gcd(m, n) = 3
m = 9797 || n = 8812 || gcd(m, n) = 1
m = 3124 || n = 5049 || gcd(m, n) = 11
m = 7495 || n = 5518 || gcd(m, n) = 1
m = 4188 || n = 5908 || gcd(m, n) = 4
m = 9488 || n = 1838 || gcd(m, n) = 2
m = 923 || n = 386 || gcd(m, n) = 1
m = 329 || n = 521 || gcd(m, n) = 1
m = 2131 || n = 9343 || gcd(m, n) = 1
m = 2220 || n = 4517 || gcd(m, n) = 1
```