import math
#
# PHI = (1 + math.sqrt(5)) / 2
# phi = -1 * 1 / PHI


def fib(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]


def len_fib(n):
    return math.floor(math.log(fib(n), 10)) + 1


if __name__ == "__main__":
    n = 12
    while True:
        length = len_fib(n)
        if length == 1000:
            print(n)
            break
        n += 1
