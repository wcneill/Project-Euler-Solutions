

def multiples(num, last):
    """
    :param num: The number to find multiples of
    :param last: The range within which you would like to find multiples of num
    :return: returns a list of all multiples up to parameter last (exclusive)
    """

    return [i for i in range(last)[::num]]


def sum_lists(*lists):
    """
    :param lists: any number of lists containing numbers
    :return: sum of the contents of all lists passed
    """

    result = 0

    for i in lists:
        result += sum(i)

    return result


def remove_dups(lst):
    """
    :param lst: The list from which you wish to remove duplicates
    :return: a new list without any duplicate items
    """

    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)

    return new_list

if __name__ == '__main__':

    comb_lists = remove_dups(multiples(3,1000) + multiples(5,1000))
    print(sorted(comb_lists))
