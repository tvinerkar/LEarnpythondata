# -------------------------------------------------------------------------
#  Let’s check how to find whether a year is a leap year in Python.
#  Leap  Year Rules--
#    A year is a leap year if:
#        1.It is divisible by 4, and
#        2.It is not divisible by 100, unless it is also divisible by 400.
# --------------------------------------------------------------------------
def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Example usage
year = int(input("Enter year:"))
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# ------ Using calender module -----

import calendar

year = 2024
print(calendar.isleap(year))   # True



