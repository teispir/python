from datetime import datetime, timezone, timedelta

def unix_to_datetime(timestamp, target_tz_offset=1):
    """
    Converts a Unix timestamp to a timezone-aware datetime.
    
    Args:
        timestamp (int): The Unix timestamp (seconds since 1970-01-01 UTC).
        target_tz_offset (int): The desired timezone offset in hours (default: GMT+1).

    Returns:
        str: Formatted datetime string in 'dd-mm-yy HH:MM:SS AM/PM' format.
    """

    # Convert timestamp to a UTC-aware datetime object
    dt_utc = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    
    # Apply the target timezone offset (e.g., GMT+1 -> offset=1)
    dt_target = dt_utc + timedelta(hours=target_tz_offset)

    # Return the formatted date and time
    return dt_target.strftime("%d-%m-%y %I:%M:%S %p")

# Example usage
timestamp = 1733213814  # Example Unix timestamp
datetime_gmt1 = unix_to_datetime(timestamp)
print("Datetime GMT+1:", datetime_gmt1)