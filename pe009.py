# Solution to project Euler #9: Find the pythagorean triple that
# sums to 1000. Implemented using Euclid's Formula, as found at
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
#
# NOTE: This method only finds primitive triplets (a, b, and c
# are coprime), but can be expanded in order to find all possible
# triplets. Luckily, the triple that sums to 1000 happened to be
# primitive.


n = 1
j = 0
sum = 0
a, b, c = 0, 0, 0

while sum != 1000:

    while sum != 1000:
        m = n + 1 + 2 * j

        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2

        sum = a + b + c

        if sum > 1000:
            break
        else:
            j += 1

    n += 1
    j = 0

print('abc =', a * b * c)