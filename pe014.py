import numpy as np
import matplotlib.pyplot as plt


def Collatz(n, evaluations={}):
    """
    Computes the length of a Collatz Sequence beginning with a specific
    number. Optimizatons at play are described below:

    1.) Recursive Limit:
        The method takes a dictionary of any previously
        calculated sequence lengths, and their associated seed value. This
        allows us to end the recursive cycle if the return value of the
        next recursive step is already known.

        Example: Let C(a_0) = {a_0, a_1, ..., a_n, ..., 1}
        where a_0 is the seed value for the sequence and the
        following elements are defined as such:

            a_n = a_(n-1)/2             if a_(n-1) even,
            a_n = 3 * a_(n-1) + 1       if a_(n-1) odd,

            So, let's take a_0 = 13:
            C(13) = {13, 40, 20, 10, 5, 16, 8, 4, 2, 1}
            C(26) = {26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1}

            As we can see, if we have the value of Collatz(13), we need
            not recompute it when calculating Collatz(26).

    2.) Restrict Search Range:
        Note that for even numbers our sequence goes like n -> n/2
        So our function, which counts the number of elements in the sequence
        goes recursively like Collatz(n) = Collatz(n/2) + 1. But this implies
        that for Collatz(2k) = Collatz(k) + 1, therefore, for all k:

        Collatz(2k) > Collatz(k).

        So, if we are searching for the maximum length of a sequence with seeds
        in some range [0, N], we may restrict our search to [N/2, N].

    :param n: The number for which we wish to evaluate Collatz stop time
    :param evaluations: A dictionary of previously evaluated Collatz numbers
            This allows for optimization by way of reducing the number of recursive
            calls. For example if we have already calculated Collatz(13), Then we know
            that Collatz(26) = 1 + Collatz(13). Why re-evaluate Collatz(13) if we already
            have that information on hand?
    :return: stop time (sequence length) of Collatz sequence with initial value n
    """
    if n in evaluations:
        return evaluations[n]
    if n == 1:
        evaluations[n] = 1
        return 1
    elif n % 2 == 0:
        evaluations[n] = 1 + Collatz(n/2, evaluations)
    else:
        evaluations[n] = 2 + Collatz((3*n + 1) / 2, evaluations)
    return evaluations[n]


max_stop_time = 0
evals = {}
iv = 0
num = 100000

for k in np.arange(1, num):
    current_stop_time = Collatz(k, evals)
    if current_stop_time > max_stop_time:
        max_stop_time = current_stop_time
        iv = k
    evals[k] = current_stop_time

print('Longest stop time: {}'.format(max_stop_time))
print('Associated Initial Value: {}'.format(iv))

lists = sorted(evals.items())
x, y = zip(*lists[:int(num)])

s = [10 * n / len(x) for n in x]
plt.scatter(x, y, s, marker='o')
plt.suptitle('Scatter Plot of first {} Collatz numbers'.format(num))
plt.xlabel('Initial Values')
plt.ylabel('Chain Length')
plt.show()
