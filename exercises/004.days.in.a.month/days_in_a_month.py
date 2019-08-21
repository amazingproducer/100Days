# Write a function that accepts a month as an integer between 1 and 12 which
# outputs the number of days in that month. This function should also accept an
# argument to return the value for leap years, which is false by default.


def days_in_month(month: int, leap_year: bool = False) -> int:
    days_by_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while 0 < month or 12 >= month:
        if leap_year == True and month == 2:
            return days_by_month[1] + 1
        return days_by_month[(month - 1)]
