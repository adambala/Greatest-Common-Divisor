# Greatest common divisor
GCD is the mathematical problem of finding the highest common factor of two non-zero integers.

This program uses [Euclidian algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) to find GCD of two integers.

## GCD function
The `gcd(a, b)` function returns the greatest common divisor of its two integer arguments `a` and `b`.

## Example
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
cd ..
### Input example:
```
Maximum possible integer: 10000
Number of tests: 10
```

### Output example:
```
m = 9431  || n = 2191  || gcd(m, n) = 1
m = 8733  || n = 8729  || gcd(m, n) = 1
m = 2506  || n = 568   || gcd(m, n) = 2
m = 9784  || n = 5412  || gcd(m, n) = 4
m = 7343  || n = 3691  || gcd(m, n) = 1
m = 7760  || n = 3890  || gcd(m, n) = 10
m = 3707  || n = 5818  || gcd(m, n) = 1
m = 352   || n = 2853  || gcd(m, n) = 1
m = 9285  || n = 2182  || gcd(m, n) = 1
m = 5968  || n = 1592  || gcd(m, n) = 8
```