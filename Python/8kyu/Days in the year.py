# https://www.codewars.com/kata/56d6c333c9ae3fc32800070f

import calendar

def year_days(year):
    if calendar.isleap(year):
        return '{0} has 366 days'.format(year)
    else:
        return '{0} has 365 days'.format(year)