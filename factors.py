import random

def factorize(n):
    if n % 2 == 0:
        return (2, n // 2)

    x, c, y, m = random.randint(1, n - 1), random.randint(1, n - 1), random.randint(1, n - 1), 1
    g, r, q = 1, 1, 1
    while g == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        g = gcd(abs(x - y), n)
        k += 1
        if k % m == 0:
            r = g
            m *= 2

    if r == n:
        while True:
            ys = (y * y + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break
        return g, n // g
    else:
        return r, n // r

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
