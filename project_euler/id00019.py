# You are given the following information, but you may prefer to do some research for yourself.
#
#   1 Jan 1900 was a Monday.
#   Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
from datetime import datetime

def sundays():
    """
    how many sundays for the 20th century
    """

    years = range(1901, 2001)
    months = range(1, 13)
    days = range(1,32)
    sundays = []

    for year in years:
        for month in months:
            for day in days:
                try:
                    d = datetime.date(datetime(year, month, day))
                    if d.weekday() == 6 and day == 1:
                        sundays.append(d)
                except ValueError:
                    # skip the errors related to the days in the month
                    continue

    return sundays
