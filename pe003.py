import math


def factors(intgr):
    """
    NOTE: This is a "Trial Division" approach and is not suitable
    for large numbers.

    :param intgr: Integer you'd like to find all factors of
    :return: a list of all factors
    """

    facts = []
    i = 1

    while i <= math.sqrt(intgr):
        if intgr % i == 0:
            if intgr / i == i:
                facts.append(i)
            else:
                facts.extend((i, intgr / i))
        i += 1

    return sorted(facts)

def prime_factors(num):
    """
    This method makes use of the fact that every composite number can be represented
    by a unique prime factorization. A corollary to this theorem is that any composite
    number contains at least one prime number less than OR equal to the square of that
    self-same number.

    Proof:

    Let a, b be two prime factors of n such that a,b > sqrt(n)
        => a*b > sqrt(n)*sqrt(n) = n
        => Contradiction!

    :param num: The number you wish to find prime factors for.
    :return: A list of factors of parameter num
    """
    facts_list = []

    while num % 2 == 0:
        facts_list.append(2)
        num /= 2

    for i in range(3, int(math.sqrt(num)) + 1 , 2):
        while num % i == 0:
            facts_list.append(i)
            num = num / i

    if num > 2:
        facts_list.append(num)

    return sorted(facts_list)


def isprime(intgr):
    """
    NOTE: This method makes use of a "Trial Division" algorithm that is not suitable
    accept for small numbers.

    :param intgr: An integer you wish to evaluate for primeness
    :return: boolean True if is prime, False if not prime
    """

    divs = factors(intgr)

    if len(divs) == 2:
        return True
    else:
        return False


if __name__ == '__main__':


    num = 997799
    print(prime_factors(num))
    print(factors(num))

    # num = 600851475143
    # print(prime_factors(num))

    print("Prime factor 9:", prime_factors(9))

