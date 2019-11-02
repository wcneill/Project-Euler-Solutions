from math import sqrt
from timeit import default_timer as timer


def factors(n):

    divs = []
    i = 1
    while i <= sqrt(n):
        if n % i == 0:
            if n / i == i:
                divs.append(i)
            else:
                divs.extend((i, n / i))

        i += 1

    return sorted(divs)


facts = 0
num = 1
count = 1

start = timer()
while facts < 500:
    facts = len(factors(num))
    count += 1
    num += count

print('{} has {} factors'.format(num - count, facts))
print('runtime {}'.format(timer() - start))