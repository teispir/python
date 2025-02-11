from datetime import datetime, timedelta

def unix_to_datetime(timestamp):
    # Convert the Unix timestamp to a datetime object
    #dt = datetime.utcfromtimestamp(timestamp)
    dt = datetime.fromtimestamp(timestamp)
    
    # Adjust for GMT+1
    dt_gmt1 = dt + timedelta(hours=1)

    # Format the output as 'dd-mm-yy HH:MM:SS AM/PM'
    return dt_gmt1.strftime("%d-%m-%y %I:%M:%S %p")

# Example usage
timestamp = 1733213814  # Example Unix timestamp
datetime_gmt1 = unix_to_datetime(timestamp)
print("Datetime GMT+1:", datetime_gmt1)