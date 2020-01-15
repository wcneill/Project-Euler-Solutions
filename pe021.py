
dictionary = {}


def proper_divisors_sum(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total


def generate_dict(n):
    for i in range(2, n):
        dictionary[i] = proper_divisors_sum(i)


def get_amicable():
    amicable_numbers = []
    for key, value in dictionary.items():

        if value != key and value in dictionary.keys():
            value2 = dictionary[value]

            if value2 == key and key not in amicable_numbers:
                amicable_numbers.append(key)
                amicable_numbers.append(value)

    return amicable_numbers


if __name__ == '__main__':
    generate_dict(10000)
    print(sum(get_amicable()))
