from inspect import isgenerator
from math import sqrt


def prime_generator(end):
    max_possible_prime_divisor = round(sqrt(end))

def prime_generator(end):
    max_possible_prime_divisor = round(sqrt(end))
    primes = [True] * (end + 1)
    primes[0] = primes[1] = False

    for i in range(2, end + 1):
        if primes[i]:
            yield i
            if i <= max_possible_prime_divisor:
                for multiple in range(i * i, end + 1, i):
                    primes[multiple] = False



gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
