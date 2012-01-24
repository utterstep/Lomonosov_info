__author__ = 'Step'
__memo__ = """
Of course I could use python 'datetime' module to solve this problem, but it would be like cheating:)
"""

def isbissextus(year):
    """
    Simple check if year is bissextus, remembering that calendar changed in 1752 year (using Gregorian)

    :type year int
    """

    return not ((year % 4) or (year % 100 == 0 and year % 400 != 0 and year > 1752))

def year_starts_with(year):
    """
    Returns first day of week in applied year.

    :type year int
    """

    days_tot = 5
    for y in xrange(1, year):
        if isbissextus(y):
            days = 366
        else:
            days = 365
        if y == 1752:
            days += 10
        days_tot += days
    return days_tot % 7

def fridays_in_year(year):
    """
    Returns number of fridays in certain year

    :type year int
    """

    bissextus = isbissextus(year)
    first_dow = year_starts_with(year)
    days = 366 if bissextus else 365
    offset = (7 - (first_dow + 3)) % 7
    days -= offset + 1
    fridays = days / 7 + 1
    return fridays

def fridays13_in_year(year):
    """
    Returns quantity of fridays, 13th in certain year.
    Ugliest method in programm, I assume..

    :type year int
    """

    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # ugly, but...

    start = year_starts_with(year)
    fridays13 = 0
    for m in xrange(12):
        if m == 1 and isbissextus(year):
            days = 29
        else:
            days = month[m]
        if (12 + start) % 7 == 4:
            fridays13 += 1
        start = (start + days) % 7
        if year == 1752 and m == 8:
            start = (start + 10) % 7

    return fridays13


def main():
    year_start = 2001
    year_end = 2020
    fridays = 0
    fridays13 = 0
    for year in xrange(year_start, year_end + 1):
        fridays += fridays_in_year(year)
        fridays13 += fridays13_in_year(year)
    print "{0}-{1}".format(fridays, fridays13)

if __name__ == '__main__':
    main()
