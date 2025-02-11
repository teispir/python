import re

def hex_to_ascii(hex_string):
    """Convert a HEX string to ASCII."""
    try:
        return bytes.fromhex(hex_string).decode('ascii')
    except Exception as e:
        return f"Error decoding hex: {e}"

def double_hex_to_ascii(hex_string):
    """Perform a double HEX to ASCII conversion."""
    try:
        first_pass = hex_to_ascii(hex_string)
        return hex_to_ascii(first_pass)
    except Exception as e:
        return f"Error in double decoding: {e}"

def process_lmisf_record(record):
    """Process a single LMISF record, converting HEX to ASCII where needed."""
    # Define the fields that need single or double conversion
    single_conversion_fields = ["sessionId", "originRealm", "destinationRealm", "userName", "sIPMethod", 
                                "userSessionId", "listOfCallingPartyAddress", "calledPartyAddress", 
                                "interOperatorIdentifiers", "accessNetworkInformation", "instanceId"]
    double_conversion_fields = ["originHost", "destinationHost"]

    # Replace HEX fields with their ASCII equivalents
    for field in single_conversion_fields:
        pattern = fr'(\b{field}\s*:\s*\')(.*?)\'H'
        record = re.sub(pattern, lambda m: f"{m.group(1)}{hex_to_ascii(m.group(2))}'", record)

    for field in double_conversion_fields:
        pattern = fr'(\b{field}\s*:\s*\')(.*?)\'H'
        record = re.sub(pattern, lambda m: f"{m.group(1)}{double_hex_to_ascii(m.group(2))}'", record)

    return record

def process_file(input_file, output_file):
    """Process the input file and write the translated content to the output file."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        content = infile.read()
        
        # Find all LMISF records in the file
        records = re.findall(r'InternalLMISF\.LMISFRecord\s*\{.*?\}', content, re.DOTALL)

        for record in records:
            translated_record = process_lmisf_record(record)
            content = content.replace(record, translated_record)

        outfile.write(content)