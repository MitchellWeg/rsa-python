import random
import math

def generate_keys(p: int, q: int):
    if p <= 0 or q <= 0:
        print("primes has to be larger than 0")
        exit(-1)

    if p == q:
        print("primes cannot be the same")
        exit(-1)

    # Step 1: find n, which is the product of the 2 prime numbers
    # p & q.
    n = p * q


    # Step 2: find the phi function of p & q using Eulers totient.
    totient = (p-1) * (q-1)

    e = random.randrange(1, totient)

    g = math.gcd(e, totient)

    # Step 3: find e, such that 1 < e < totient
    # (did not find an elegant way to do this, so just brute force it.)
    while g != 1:
        e = random.randrange(1, totient)
        g = math.gcd(e, totient)

    # Step 4: Find the multiplicative inverse of e and the totient.
    d = multiplicative_inverse(e, totient)

    return ((e,n), (d,n))

def eulers_totient(p, q):
    return (p-1) * (q-1)

def multiplicative_inverse(e, t):
    return pow(e, -1, t)
