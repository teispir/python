def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if(month == 1):
        return int(31)
    if(month == 2):
        if is_year_leap(year):
            return int(29)
        else:
            return int(28)
    if(month == 3):
        return int(31)
    if(month == 4):
        return int(30)
    if(month == 5):
        return int(31)
    if(month == 6):
        return int(30)
    if(month == 7):
        return int(31)
    if(month == 8):
        return int(31)
    if(month == 9):
        return int(30)
    if(month == 10):
        return int(31)
    if(month == 11):
        return int(30)
    if(month == 12):
        return int(31)
    
def day_of_year(year, month, day):
    
    countdays = 0
    
    for i in range(1,month):
        daysinmonth =  days_in_month(year,i)
        countdays = countdays + daysinmonth

    return day + countdays
    
dayofyear = day_of_year(2001, 10, 7)
print("day_of_year", dayofyear)