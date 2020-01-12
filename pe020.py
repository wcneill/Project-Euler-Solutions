
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def sum_digits(n):
    sums = 0
    digits = str(n)
    for i in digits:
        print(i)
        sums += int(i)

    return sums


if __name__ == '__main__':

    print(sum_digits(fact(100)))
