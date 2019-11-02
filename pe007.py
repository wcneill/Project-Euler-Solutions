import math

def is_prime(num):
    """
    Every composite number N has a factor less than or equal to
    sqrt(N). See proof outlined in comments of Exercise 3 - pe003.py
    If no factor is found by sqrt(N), then the number must be prime.

    So, this algorithm iterates through all possible prime numbers less
    than sqrt(N). We speed this up by making use of the fact that every
    prime number p can be represented as

    p = 6k +/- 1

    Proof:
    It can be shown that all integers are in the set {0,1,2,3,4,5}
    modulo 6.

    Therefore:

    x = 6k                  (composite)
    x = 6k + 1              (possibly prime)
    x = 6k + 2 = 2(3k + 1)  (composite)
    x = 6k + 3 = 3(2k + 1)  (composite)
    x = 6k + 4 = 2(3k + 2)  (composite)
    x = 6k + 5 = 6m - 1     (possibly prime)

    So, the only options for prime numbers are 6k + 1 or 6k - 1.

    :param num: The number to determine primality of
    :return: Boolean (is prime?)
    """

    if num == 1:
        return False
    if num == 2:
        return True
    if num == 3:
        return True
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False

    stop = math.floor(math.sqrt(num))
    i = 5

    while i <= stop:

        # We are checking each number i = 6k - 1
        if num % i == 0:
            return False

        # We are checking i = 6k + 1
        if num % (i + 2) == 0:
            return False

        i += 6

    return True

def prime_counter(n):
    """
    Gets a list of the first n prime numbers.
    :param n: the prime number you are looking for
    :return: a list of prime numbers up to the nth prime number
    """
    primes = [2]
    number = 3
    count = 1

    while count != n:
        if is_prime(number):
            primes.append(number)
            count += 1

        number += 2

    return primes

if __name__ == '__main__':

    print(prime_counter(10001)[-1])