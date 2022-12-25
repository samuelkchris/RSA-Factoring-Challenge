import math

def factorize(n):
    if n % 2 == 0:
        return (2, n // 2)

    # Find a smooth number using the quadratic sieve
    a = math.floor(math.sqrt(n))
    b2 = a*a - n
    b = int(math.sqrt(b2))
    while b*b != b2:
        a += 1
        b2 = a*a - n
        b = int(math.sqrt(b2))

    # Find the prime factors of the smooth number
    factors = prime_factors(b2)

    # Try to lift the factors of the smooth number to factors of n
    for p in factors:
        pe = p
        while pe <= a:
            pe *= p
        x = ((pe * a) + b) // p
        y = ((pe * a) - b) // p
        g = gcd(x - y, n)
        if g > 1:
            return (g, n // g)

def prime_factors(n):
    # Find the prime factors of n using trial division
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
