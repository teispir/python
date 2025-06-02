def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def get_days_in_month(year, month):
    """
    Returns the number of days in a given month for a specified year
    without using the calendar module.
    
    :param year: The year (e.g., 2023)
    :param month: The month number (1 for January, 2 for February, etc.)
    :return: The number of days in the specified month
    """
    #####################################################################
    # List with the number of days for each month, assuming a common year
    # February is set to 28 days by default
    #####################################################################
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #########################################################################
    # Check for leap year and update February days to 29 if it is a leap year
    #########################################################################
    if month == 2 and is_year_leap(year):
        return 29

    # Return the number of days in the specified month
    return days_in_month[month - 1]

    
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = get_days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")