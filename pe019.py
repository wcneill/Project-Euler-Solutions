
monthdict = {
    1: 31,
    2: 28,
    3: 31, 
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

ly_monthdict = {
    1: 31,
    2: 29,
    3: 31, 
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

leap_year = False
sundays_on_first = 0
first_sunday = 6

for year in range(1901, 2001):
    if year % 4 == 0 and year % 100 != 0:
        leap_year = True
    elif year % 100 == 0 and year % 400 == 0:
        leap_year = True
    else:
        leap_year = False

    for month in range(1, 13):

        if first_sunday == 1:
            sundays_on_first += 1

        curr_sunday = first_sunday
        if leap_year:
            while curr_sunday < ly_monthdict[month]:
                curr_sunday += 7

            first_sunday = curr_sunday - ly_monthdict[month]
        else:
            while curr_sunday < monthdict[month]:
                curr_sunday += 7

            first_sunday = curr_sunday - monthdict[month]

print(sundays_on_first, "Sundays occured on the first of the month")
