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
        return 31
    if(month == 2):
        if is_year_leap(year):
            return 29
        else:
            return 28
    if(month == 3):
        return 31
    if(month == 4):
        return 30
    if(month == 5):
        return 31
    if(month == 6):
        return 30
    if(month == 7):
        return 31
    if(month == 8):
        return 31
    if(month == 9):
        return 30
    if(month == 10):
        return 31
    if(month == 11):
        return 30
    if(month == 12):
        return 31
    
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")