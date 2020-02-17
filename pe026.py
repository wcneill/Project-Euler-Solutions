
"""

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
    N = 1000
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
