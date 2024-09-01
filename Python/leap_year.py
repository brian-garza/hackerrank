################################
####  Leap Year Calculator  ####
################################

def is_leap(year):
    leap = False
    if (year % 400 == 0) and (year % 100 == 0):
        leap = True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 ==0) and (year % 100 != 0):
        leap = True

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        leap = False

    return leap

year = int(input())
print(is_leap(year))