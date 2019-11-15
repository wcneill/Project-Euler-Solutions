
ones_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten'
}

teens_dict = {
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen"
}

tens_dict = {
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}


def num_2_word(num):
    if num == 1000:
        return "one thousand"

    if 99 < num < 1000:

        if num % 100 == 0:
            # num = 300
            hunds = num/100  # = 3
            return ones_dict[hunds] + " hundred"  # "three hundred"

        # get hundreds place:
        xh = num - (num % 100)  # = 352 - 52 = 300
        hunds = xh/100  # = 3

        # get tens place
        xt = num - xh - (num % 10)  # 352 - 300 - 2 = 50
        tens = xt/10  # = 50/10 = 5

        # get ones place
        ones = num % 10  # 352 % 10 = 2

        # case: No place contains zero, tens place greater than 1
        if tens != 0 and tens != 1 and ones != 0:
            return ones_dict[hunds] + " hundred and " + tens_dict[tens] + "-" + ones_dict[ones]

        # case: No place contains zero, tens place equals 1
        if tens == 1 and ones != 0:
            return ones_dict[hunds] + " hundred and " + teens_dict[ones]

        # case: Ones place contains zero, tens place greater than 1
        if tens != 0 and tens != 1 and ones == 0:
            return ones_dict[hunds] + " hundred and " + tens_dict[tens]

        # case: Ones place contains zero, tens place equal to one
        if tens == 1 and ones == 0:
            return ones_dict[hunds] + " hundred and ten"

        # Case: tens place contains zero
        if tens == 0:
            return ones_dict[hunds] + " hundred and " + ones_dict[ones]

    if 9 < num < 100:

        # case num = 10
        if num == 10:
            return "ten"

        # case: num % 10 = 0
        if num % 10 == 0:
            return tens_dict[num/10]

        xt = num - (num % 10)
        tens = xt/10
        ones = num % 10

        # case: number is in teens
        if tens == 1:
            return teens_dict[ones]

        # case: number is greater than 19
        if tens != 1:
            return tens_dict[tens] + "-" + ones_dict[ones]

    if num < 10:
        return ones_dict[num]


if __name__ == '__main__':

    numlist = []
    for i in range(1, 1001):

        numlist.append(num_2_word(i).replace(' ', '').replace('-', ''))

    s = "".join(numlist)
    print(len(s))
