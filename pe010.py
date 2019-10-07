import pe007 as p7
from timeit import default_timer as timer

def runtime(func, args):
    """
    This method will run and return total run time of any function passed
    to it.
    :param func: The function to time.
    :param args: Positional arguments for the function
    :return: Runtime in fractional seconds
    """
    start = timer()
    func(*args)
    print(timer() - start)

def sumprime(stop):
    """
    This method sums primes below a given range (exclusive)
    :param stop: integer value. sumprime will sum all of the prime numbers
    below "stop"
    :return: sum of all primes less than the parameter "stop"
    """

    stop = int(stop)
    sum = 0
    i = 1

    while i < stop:

        if p7.is_prime(i):
            sum = sum + i
            i += 1
        else:
            i += 1

    print(sum)
    return sum

if __name__ == '__main__':

    runtime(sumprime, [2e6])