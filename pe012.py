from math import sqrt
from timeit import default_timer as timer


def fact_count(n):

    cnt = 0
    i = 1
    while i <= sqrt(n):
        if n % i == 0:
            if n / i == i:  # For case of perfect square
                cnt += 1
            else:
                cnt += 2
        i += 1
    return cnt


facts = 0
num = 1
count = 1

start = timer()
while facts < 500:
    facts = fact_count(num)
    count += 1
    num += count

print('{} has {} factors'.format(num - count, facts))
print('runtime {}'.format(timer() - start))
