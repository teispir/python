from datetime import datetime, timedelta

def hex_to_datetime(hex_string):
    print(f"***************[5] HEX_TO_DATETIME")
    print(f"provided hex_string: {hex_string}")

    try:
        # Converti il valore HEX in un intero
        timestamp = int(hex_string, 16)
        print(f"timestamp: {timestamp}")
        
        # Calcola la data usando l'epoca Unix (1900-01-01)
        date = datetime(1900, 1, 1) + timedelta(seconds=timestamp)

        # Formatta la data nel formato desiderato
        formatted_date = date.strftime("%d-%m-%y %I:%M:%S %p")
        print(f"formatted_date: {formatted_date}")
        return formatted_date

    except ValueError as e:
        print(f"Error converting hex to datetime: {e}")
        return None

if __name__ == "__main__":
    
    mytime = 3942202614-2208988800
    print(f"mytime: {mytime}")
    
    hex_to_datetime(mytime)