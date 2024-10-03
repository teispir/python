def hex_to_ascii(hex_str):
    ascii_str = ""
    # Loop through the hex string two characters at a time
    for i in range(0, len(hex_str), 2):
        # Convert two characters at a time from hex to decimal
        decimal_value = int(hex_str[i:i+2], 16)
        # Convert the decimal value to its ASCII character equivalent
        ascii_str += chr(decimal_value)
    return ascii_str

def HexToAsciiConverter(input.txt, output):
    with open(input.txt, 'r') as f_in:
        hex_data = f_in.read().strip()  # Read the hex data from input file

    ascii_data = hex_to_ascii(hex_data)

    with open(output.txt, 'w') as f_out:
        f_out.write(ascii_data)  # Write the ASCII data to output file

if __name__ == "__main__":
    input.txt = input("Enter the path of the input text file: ")
    output = input("Enter the path of the output text file: ")
    HexToAsciiConverter(input.txt, output)
    print("Conversion completed. Output written to", output)
