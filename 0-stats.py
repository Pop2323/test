#!/usr/bin/python3

import sys


def print_msg(dict, total_size):
    """Prints the total file size and the count of each status code."""
    print("File size: {}".format(total_size))
    for key, val in sorted(dict.items()):
        if val != 0:
            print("{}: {}".format(key, val))

total_size = 0
code = ""
count = 0

# Dictionary to count occurrences of each HTTP status code
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        # Splitting the input line and reversing it
        splited = line.split()[::-1]
        
        # Check if the split line has at least two elements
        if len(splited) > 1:
            count += 1

            # Only process the first 10 lines
            if count <= 10:
                total_size += int(splited[0])
                code = splited[1]

                # If the status code is in the dictionary, increment its count
                if code in status_codes:
                    status_codes[code] += 1

            # Every 10 lines, print the message and reset the count
            if count == 10:
                print_msg(status_codes, total_size)
                count = 0

finally:
    # Ensure the final message is printed when the script ends
    print_msg(status_codes, total_size)