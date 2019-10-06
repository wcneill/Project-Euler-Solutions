import pe003 as pe
from collections import Counter


def lcm(iterable):
    """
    A faster version for finding the least common multiple of all the
    numbers from 1 to 20. My methodology here is based on the
    Wikipedia article "Least Common Multiple". Therein two different
    simple methods were described: 1.) Using the Greatest Common
    Denominator and 2.) Using prime factorization. Since I peaked at
    a solution found online using method 1, I decided to take a stab at
    completing the exercise using method 2 on my own.

    In simple terms, if one wants to know the least common multiple
    of a set of numbers lcm(k_1, k_2, ... , k_n), one need only find
    the prime factorization of each k_i, and count the highest power of
    each recorded prime factor. Once the highest power of each prime is found,
    We multiply each prime to its highest found power to get our answer

    EXAMPLE: We want to know lcm(2,4,5,6,8)

    Prime Factorizations of each k_i:
    2 -> 2        (2^1)
    4 -> 2, 2     (2^2)
    5 -> 5        (5^1)           *** highest power of 5
    6 -> 2, 3     (2^1), (3^1)    *** highest power of 3
    8 -> 2, 2, 2  (2^3)           *** highest power of 2

    Therefore, lcm(2, 4, 5, 6, 8) = 2^3 * 3^1 * 5^1 = 120

    :param iterable: the set of integers you wish to find the LCM of
    :return: the LCM of all numbers in the iterable parameter
    """
    prime_facts = {}
    lcm = 1

    for k in iterable:

        kfacts = pe.prime_factors(k)
        print("factorization of", k, "is", kfacts)

        for i in kfacts:
            count = Counter(kfacts)[i]

            if i not in prime_facts.keys():
                prime_facts[i] = count

            elif i in prime_facts.keys() and prime_facts[i] < count:
                prime_facts[i] = count

    for f in prime_facts.keys():
        lcm = lcm * f**prime_facts[f]

    return lcm


if __name__ == '__main__':

    print(lcm([8,9,21]))