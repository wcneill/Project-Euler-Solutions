
def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    prod = 1
    for i in range(2, n + 1):
        prod *= i

    return prod


if __name__ == '__main__':

    n = 20
    k = 20

    paths = fact(n + k) / (fact(n) * fact(k))
    print(paths)
