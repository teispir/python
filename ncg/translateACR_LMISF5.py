import re

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

def process_lmisf_record(record):
    """Process a single LMISF record, converting HEX to ASCII where needed."""
    print(f"\nProcessing record: {record}\n")  # Debug: Show the full record before processing

    single_conversion_fields = [
        "sessionId", "originRealm", "destinationRealm", "userName", "sIPMethod", 
        "userSessionId", "listOfCallingPartyAddress", "calledPartyAddress", 
        "interOperatorIdentifiers", "accessNetworkInformation", "instanceId"
    ]
    double_conversion_fields = ["originHost", "destinationHost"]

    def debug_substitution(m, conversion_type):
        original_hex = m.group(2)
        try:
            if conversion_type == "single":
                ascii_value = hex_to_ascii(original_hex)
            else:
                ascii_value = double_hex_to_ascii(original_hex)
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

    print(f"Processed record: {record}\n")  # Debug: Show the record after all processing
    return record

def process_file(input_file, output_file):
    """Process the input file and write the translated content to the output file."""
    print(f"**********[1] PROCESS_FILE")
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        content = infile.read()
        
        # Find all LMISF records in the file
        # This pattern captures everything between the outermost braces of each record
        records = re.findall(r'InternalLMISF\.LMISFRecord\s*\{.*?\}', content, re.DOTALL)
        print(f"**********[1] PROCESS_FILE:records {records}" )
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