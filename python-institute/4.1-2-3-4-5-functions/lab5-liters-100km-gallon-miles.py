def liters_100km_to_miles_gallon(liters):
    """Convert liters per 100km to miles per gallon."""
    miles_per_gallon = 235.215 / liters
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    """Convert miles per gallon to liters per 100km."""
    liters = 235.215 / miles
    return liters

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))