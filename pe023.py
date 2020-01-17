import math


def prop_divisors(x):
    prop_divs = [1]
    i = 2

    while i <= math.sqrt(x):
        if x % i == 0:
            if x/i == i:
                prop_divs.append(i)
            else:
                prop_divs.extend((x/i, i))
        i += 1
    return prop_divs


def isAbundant(x):
    if sum(prop_divisors(x)) > x:
        return True
    else:
        return False

# We are tasked with finding the sum of all numbers which cannot
# be expressed as a sum of two abundant numbers. An abundant number
# n is one whose proper factors sum to a number larger than it.
# An example is 12, which has proper factors 1,2,3,4,6. There sum
# is 16, and therefore 12 is an abundant number.
#
# We are told that all numbers greater than 28123 can be expressed
# as a sum of abundant numbers. Since we wish to find all numbers
# that CANNOT be expressed as sums of abundant numbers, we say that
# our universe will be U = {1,2,...,2813}.
#
# Next, we wish to find the set A of all of the abundant numbers in
# our universe.
#
# After all abundant numbers are found, we must find all possible sums
# of these numbers. We may exclude any sum that falls outside of our
# universe.
#
# At this point we have 3 sets:
#   1.) U = {1,...,28123} (Our universe of inspection)
#   2.) A = {12, 18, 20, 24,...} (Our abundant numbers)
#   3.) S = {24, 30, 32, 36,...} (All possible sums of elements of set A)
#
# Keeping in mind that our task is to find the set N of all numbers
# that are not the sum of two abundant numbers.
#
# We know that set U is ALL the possible numbers might care to check.
# We also know that the set S is the set of numbers that are sums of
# abundant numbers. So to get down to the numbers we really want, we simply
# subtract those numbers in the set S from our universe U. In set notation
# this is written as N = U\S, which is the rough equivalent of subtraction
# in set theory.


universe = set(range(1, 28124))
abundant_numbers = set()
sums_of_abundant = set(range(48, 28124, 2))

for n in universe:
    if isAbundant(n):
        abundant_numbers.add(n)

for a in abundant_numbers:
    for a_2 in abundant_numbers:
        result = a + a_2
        if result < 28124:
            sums_of_abundant.add(result)

not_abundant_sum = universe - sums_of_abundant
print(sum(not_abundant_sum))
