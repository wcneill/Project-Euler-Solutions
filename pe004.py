

def is_palindrome(num):
    """
    Determines if a number is a palindrome
    :param num: An integer or a string.
    :return: Boolean (is palindrome?)
    """

    test = list(str(num))
    if test == test[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    """
    Checks finds the largest product of numbers between 100 and 1000 that is 
    also a palindrome. 
    """

    brk = False
    pals = []

    for i in range(100, 1000):
        for k in range(100, 1000):
            if is_palindrome(i * k):
                pals.append(i * k)

    pals.sort()
    print(pals[-1])