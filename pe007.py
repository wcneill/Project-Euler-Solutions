import math

def is_prime(num):
    """
    Every composite number N has a factor less than or equal to
    sqrt(N). See proof outlined in comments of Exercise 3 - pe003.py
    If no factor is found by sqrt(N), then the number must be prime.

    :param num: The number to determine primality of
    :return: Boolean (is prime?)
    """
    facts = [i for i in range(2, int(math.sqrt(num)) + 1) if num % i == 0]

    if len(facts) == 0:
        return True
    else:
        return False



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