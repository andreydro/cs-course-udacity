# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

def daysBetweenDates(year_1, month_1, day_1, year_2, month_2, day_2):
    days = 0
    while not(year_1 == year_2 and month_1 == month_2 and day_1 == day_2):
        if days_of_months[(month_1 - 1)] == day_1:
            if (month_1 == 2) and leap_year(year_1):
                days, month_1, day_1 = days + 1, month_1 + 1, 0
            elif month_1 == 12:
                year_1, month_1 = year_1 + 1, 0
            else:
                month_1, day_1 = month_1 + 1, 0
        else:
            day_1 = day_1 + 1
            days = days + 1
    return days



# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
