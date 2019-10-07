import math

def is_prime(num):
    """
    Every composite number N has a factor less than or equal to
    sqrt(N). See proof outlined in comments of Exercise 3 - pe003.py
    If no factor is found by sqrt(N), then the number must be prime.

    Additionally, this algorithm makes use of the fact that any
    numbers "n" greater than 3 can be represented as:

    n = 6k +/- 1

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

        # For any num = 5 + 6k, there is an integer n
        # such that 5 + 6k = 6n - 1
        if num % i == 0:
            return False

        # Because, for any integer k:
        # 5 + 6k + 2 = 6n - 1 + 2 = 6n + 1
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