def isLeapYear(year):
    if year % 400 == 0: return True
    elif year % 100 == 0: return False
    else: return year % 4 == 0
