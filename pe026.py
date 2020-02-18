
"""
There are three cases that can occur when it comes to repeating decimals and integer inverses:

CASE1: Terminating Decimals
CASE2: Purely repeating decimal
CASE3: Repeating decimal cycle AFTER a non repeating section of decimals


CASE 1: 1/n produces a terminating decimal number if and only if n= (2^x)(2^y).

    Assume that n is of the form (2^x)(5^y). Choose d = max{x, y}
    => Then 10^d/n = (2^d)(5^d)/(2^x)(5^y)
    => Without loss of generality, assume that d = max{x, y} = x
    => 10^d/n = (2^x)(5^x)/(2^x)(5^y) =  5^(x - y) = m, which is an integer.
    => we may then write 1/n = m/(10^d) = 0.0...0m, where the number of preceding zeros is d-1.


CASE 2: 1/n produces a purely periodic, repeating decimal if and only if n is coprime to 10:

    Part A:  If n coprime to 10 => 1/n is a periodic repeating decimal

        First, let us find an equivalent mathematical expression for "periodic, repeating decimal":

        Let 1/n = r be of the form 0.c, where c is a repeating number with period k

            (ex 0.123123, where 123 repeats forever)

        => there exits a k such that (10^k)/n = shares the same decimal part as r = 1/n for this product results in a
        simple shift left, where the shift is k digits

            example:  (10^3)(0.123...) = 123.123...

        => (10^k)r - r = m, where m is an integer.

            example: 123.123... - 0.123 = 123

        => (10^k - 1)r = (10^k - 1)/n = m
        => (10^k - 1) mod n = 0
        => 10^k mod n = 1 (and interesting to us, the smallest k where this is true is the period of repitition!)

        Therefore, if 1/n is a purely periodic, repeating decimal, there exists a k, such that 10^k mod n = 1

        Using this definition, we can proceed with the proof:

        If we consider the remainders of {10, 10^1, 10^2, ...} when divided by n we see that there are infinitely
        many numbers but only finite possible remainders.
        => there exists two natural numbers p and q such that p < q where n | 10^p and n | 10^q.
        => n | 10^q - 10^p
        => n | 10^p * (10^(q-p) - 1)
        => since n is coprime with 10, it cannot divide 10^p and so
        => n | 10^(q-p) - 1 => 10^(q-p) mod n = 1, which is our above established definition of a repeating decimal
        when we set k = q - p.

    Part B: If 1/n is a periodic decimal => n is coprime to 10 (By Contradiction)

        Assume that n and 10 are NOT coprime. That is to say, there is an natural number p > 1 that divides both
        10 and n.

        By definition of periodic decimal expansion, there exists a k and l such that 10^k - 1 = ln,
        => 10^k - nl = 1
        => since d divides both 10^k and any integer multiple of n, d divides 10^k - nl = 1
        => but since d > 1, this provides a contradiction


CASE 3: Assume r = 1/n, where n = (2^x)(2^y)n', where n' is coprime to 10.
    The decimal expansion of any rational number is finite or eventually periodic, so it must be that the natural
    numbers n not covered by the previous two cases are precisely those such that 1/n has an infinite, not immediately
    periodic decimal expansion.

    We may put this third case to use for counting the length of the periodic portion of an eventually periodic
    decimal exansion:

    Assume r = 1/n has an eventually repeating decimal expansion =>  n = (2^x)(2^y)n'

    => there exists an integer d such that (10^d)/n has a purely repeating decimal part.
    => further, there exists an integer k such that 10^(k + d) has the same decimal part as 10^d.
    => (10^(k + d)  / n) - (10^k / n) = c is an integer.
    => c = (10^d)(10^k - 1)/n
    => remembering that n = (2^x)(5^y)n', choose d = max{x, y} .
    => (10^d)(10^k - 1)/n = K(10^k - 1)/n' = c , where c is an integer and where K is the leftover power of 10 from
    the cancellation of 10^d/n
    => because c is an integer, we know that n' must either divide K or 10^k - 1. However, since K is a power of 10,
    we know that n' cannot divide it and therefore 10^k - 1 mod n' = 0.
    =>  10^k mond n' = 1.
    => solving for the smallest k such that the last line is true gives us the period of the repeating portion.


"""



def makeCoPrime(n):
    while (n % 2) == 0:
        n = n / 2
    while (n % 5) == 0:
        n = n / 5
    return int(n)

def modSolve(n):
    k = 1
    currVal = 10
    while True:
        if currVal % n == 1:
            return k
        k += 1
        currVal = pow(10, k, n)


if __name__ == '__main__':

    longest_cycle = 0
    longest_index = 0
    N = 10000
    cycle_lengths = {}
    for n in range(1, N):
        n_prime = makeCoPrime(n)
        if n_prime != 1:
            k = modSolve(n_prime)
            cycle_lengths[n] = k

            if k > longest_cycle:
                longest_cycle = k
                longest_index = n

        else:
            cycle_lengths[n] = 0

    print("The longest repeating decimal cycle of 1/n"
          " for n=0 to n={} occurs at 1/{}: {}".format(N - 1, longest_index,  cycle_lengths[longest_index]))
