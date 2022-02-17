"""
Problem 19: Counting Sundays
----------------------------------
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import datetime


def solution():
    start_date = datetime.date(1901, 1, 1)
    end_date = datetime.date(2000, 12, 31)
    time_period = end_date - start_date

    current_day = start_date
    sunday_count = 0

    for x in range(time_period.days):
        day_of_month = current_day.day
        day_of_week = current_day.weekday()

        if day_of_month == 1 and day_of_week == 6:
            sunday_count += 1
        current_day += datetime.timedelta(1)

    print(sunday_count)

    return
