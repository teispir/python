import re
from datetime import datetime, timezone, timedelta

def hex_to_ascii(hex_string):
    """Convert a HEX string to ASCII."""
    print(f"***************[3] HEX_TO_ASCII") 

    try:
        print(f"Converting HEX to ASCII: {hex_string}")  # Debug: Show HEX input
        ascii_result = bytes.fromhex(hex_string).decode('ascii')
        print(f"Resulting ASCII: {ascii_result}")  # Debug: Show ASCII output
        return ascii_result
    except Exception as e:
        print(f"Error decoding hex: {e}")  # Debug: Show error
        return f"Error decoding hex: {e}"

def double_hex_to_ascii(hex_string):
    """Perform a double HEX to ASCII conversion."""
    print(f"***************[4] DOUBLE_HEX_TO_ASCII")
    try:
        first_pass = hex_to_ascii(hex_string)
        print(f"First pass result: {first_pass}")  # Debug: Show first pass result
        second_pass = hex_to_ascii(first_pass)
        print(f"Second pass result: {second_pass}")  # Debug: Show second pass result
        return second_pass
    except Exception as e:
        print(f"Error in double decoding: {e}")  # Debug: Show error
        return f"Error in double decoding: {e}"

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
    
def process_lmisf_record(record):
    """Process a single LMISF record, converting HEX to ASCII where needed."""
    print(f"\nProcessing record: {record}\n")  # Debug: Show the full record before processing

    single_conversion_fields = [
        "sessionId", "originRealm", "destinationRealm", "userName", "sIPMethod", 
        "userSessionId", "listOfCallingPartyAddress", "calledPartyAddress", 
        "interOperatorIdentifiers", "accessNetworkInformation", "instanceId", 
        "listOfCallingPartyAddress", "calledPartyAddress", "sIP-URI", "interOperatorIdentifiers", 
        "originatingIOI", "iMSChargingIdentifier"
    ]
    double_conversion_fields = ["originHost", "destinationHost"]

    time_conversion_fields = ["eventTimestamp", "listOfTimeStamps", "sipRequestTimestamp", "sipResponseTimestamp"]

    def debug_substitution(m, conversion_type):
        original_hex = m.group(2)
        try:
            if conversion_type == "single":
                ascii_value = hex_to_ascii(original_hex)
            elif conversion_type == "double":
                ascii_value = double_hex_to_ascii(original_hex)
            else:
                unixtimestamp = int(original_hex)-2208988800
                print(f"unixtimestamp: {unixtimestamp}")
                ascii_value = unix_to_datetime(unixtimestamp)

            print(f"Field: {m.group(1)}, Original HEX: {original_hex}, Converted ASCII: {ascii_value}")
            return f"{m.group(1)}{ascii_value}'"
        except Exception as e:
            print(f"Error converting {m.group(1)}: {e}")
            return m.group(0)  # Return original if there's an error

    for field in single_conversion_fields:
        pattern = fr'(\b{field}\s*:\s*\')([0-9A-Fa-f]*)\'H'
        record = re.sub(pattern, lambda m: debug_substitution(m, "single"), record)

    for field in double_conversion_fields:
        pattern = fr'(\b{field}\s*:\s*\')([0-9A-Fa-f]*)\'H'
        record = re.sub(pattern, lambda m: debug_substitution(m, "double"), record)

    for field in time_conversion_fields:
        pattern = fr'(\b{field}\s*:\s*\')([0-9A-Fa-f]*)\'H'
        record = re.sub(pattern, lambda m: debug_substitution(m, "time"), record)

    print(f"Processed record: {record}\n")  # Debug: Show the record after all processing
    return record

def find_lmisf_records(content):
    records = []
    start = 0
    while True:
        start = content.find('InternalLMISF.LMISFRecord', start)
        if start == -1:
            break
        open_braces = 0
        i = start
        while i < len(content):
            if content[i] == '{':
                open_braces += 1
            elif content[i] == '}':
                open_braces -= 1
                if open_braces == 0:
                    records.append(content[start:i + 1])
                    break
            i += 1
        start = i + 1
    return records

def process_file(input_file, output_file):
    """Process the input file and write the translated content to the output file."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        content = infile.read()
        
        # Find all LMISF records in the file using custom parsing
        records = find_lmisf_records(content)

        for record in records:
            print(f"Original record: {record}")  # Debug: Show the full record before processing
            translated_record = process_lmisf_record(record)
            content = content.replace(record, translated_record)

        outfile.write(content)

if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the path to the output file: ")
    process_file(input_file, output_file)
    print(f"File processed successfully. Translated content saved to {output_file}.")