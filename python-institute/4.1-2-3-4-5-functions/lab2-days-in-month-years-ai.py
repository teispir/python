import calendar

def get_days_in_month(year, month):
    """
    Returns the number of days in a given month for a specified year.
    
    :param year: The year (e.g., 2023)
    :param month: The month number (1 for January, 2 for February, etc.)
    :return: The number of days in the specified month
    """
    # Use calendar.monthrange to get the number of days in the month
    _, num_days = calendar.monthrange(year, month)
    return num_days
    
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